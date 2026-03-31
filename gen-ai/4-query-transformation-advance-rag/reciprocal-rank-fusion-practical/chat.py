import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from collections import defaultdict

load_dotenv()

COLLECTION_NAME = "learning_vectors_with_reciprocal-rank-fusion"

qdrant_url = os.getenv("QDRANT_URL")

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
  url=qdrant_url,
  collection_name=COLLECTION_NAME,
  embedding=embedding_model
)

def generate_parallel_queries(user_query: str, n: int = 3):
  prompt = f"""
    Generate {n} different version of the following query.
    Each version should have a slightly different phrasing or perspective, but it should be related to the original query and preserve the original intent.
    
    Original query: {user_query}  
    
    Output: Return only the queries, one per line, without numbering or bullets.  
  """
  
  response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a query transformation expert. Generate alternative versions of queries to improve search results."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7  # Some creativity for variations
    )
  
  generated_queries = response.choices[0].message.content.strip().split('\n')

  # Clean up any empty lines or numbering
  generated_queries = [q.strip().lstrip('0123456789.-) ') for q in generated_queries if q.strip()]
  
  # Return original query + generated alternatives
  return [user_query] + generated_queries[:n]

def reciprocal_rank_fusion(results: list[list], k:int = 60):
  doc_scores = defaultdict(lambda: {"doc": None, "score": 0})
  
  # Calculate the scores based on the result docs
  for result in results:
    for rank,doc in enumerate(results,start=1):
      doc_id = hash(doc.page_content)
      doc_scores[doc_id]["doc"] = doc
      doc_scores[doc_id]["score"] += 1.0 / (k + rank)
      
  # Sort by score (highest first)
  sorted_docs = sorted(doc_scores.values(), key=lambda x: x["score"], reverse=True)
  
  return [item["doc"] for item in sorted_docs]

# Main Rag Flow

question = input("Type your question here: ")

print("\n Generating query variations...")
parallel_queries = generate_parallel_queries(question)

print("\n Query variations:")
for i,q in enumerate(parallel_queries, 1):
  print(f" {i}. {q} ")
  
print("\n Retrieving documents...")  

all_results = []
for query in parallel_queries:
  results = vector_db.similarity_search(query=query, k=4)
  all_results.append(results)
  
print("Applying RRF...")

ranked_results = reciprocal_rank_fusion(all_results)

print(f"✅ Got {len(ranked_results)} ranked documents\n")

# Take top 3 results
top_results = ranked_results[:6]

context = "\n\n---\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in top_results])

SYSTEM_PROMPT = f"""
  You are an helpful AI Assistant who answers users query based on the available context retrieved.
  
  You should only answer the user based on the following context and navigate the user to open the right page number to know more. If you don't get the answer from the available context for the user question then let the user know that you don't know the answer of the user question.
  
  Context: {context}
"""

print("Generating answer...")
chat_completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
)

print(f"🤖: {chat_completion.choices[0].message.content}")