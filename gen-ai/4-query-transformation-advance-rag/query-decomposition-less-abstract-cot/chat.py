import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTION_NAME = "learning_vectors_with_query_decomposition_less_abstract_cot"

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

def decompose_query(query: str):
  prompt = f"""
    Break down this user query into 2-3 simpler sub-queries that cover the different aspects:
    
    Query: {query}
    
    Output: Return only the sub-queries, one per line.
  """
  
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.5
  )
  
  sub_queries = response.choices[0].message.content.strip().split('\n')
  sub_queries = [q.strip() for q in sub_queries if q.strip()]
  
  return sub_queries

def generate_llm_response_for_subquery(sub_query: str):
  prompt = f"""
    Please provide a brief explanation for this query: {sub_query}. Keep it concise (2-3 sentences).
  """
  
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
  )
  
  return response.choices[0].message.content.strip()

  
def search_with_enriched_query(sub_query: str, llm_response: str, k: int = 4):
  enriched_query = f"{sub_query}. {llm_response}"
  
  results = vector_db.similarity_search(query=enriched_query,k=k)
  return results  

# Main Rag Flow

question = input("Type your question here: ")

print("\n Decomposing query into sub-queries...")
sub_queries = decompose_query(question)

print(f"Sub-queries ({len(sub_queries)}):")

  
print("\n Processing each sub-query with LLM...")  

all_results = []
seen_contents = set()

for i, sub_query in enumerate(sub_queries, 1):
  print(f"[{i}/{len(sub_queries)}] Processing: {sub_query}")
  
  # Get LLM response for this sub-query
  llm_response = generate_llm_response_for_subquery(sub_query)
  print(f"     LLM says: {llm_response[:80]}...")
  
  results = search_with_enriched_query(sub_query, llm_response, k=4)
  
  # Remove duplicates
  for result in results:
    content_hash = hash(result.page_content)
    if content_hash not in seen_contents:
      seen_contents.add(content_hash)
      all_results.append(result)
      
print(f"✅ Total unique documents: {len(all_results)}\n")

top_results = all_results[:8]
      
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