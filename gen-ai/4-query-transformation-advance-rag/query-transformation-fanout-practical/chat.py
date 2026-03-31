import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTION_NAME = "learning_vectors_with_query_transformation"

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

def retrieve_with_parallel_queries(queries: list[str], top_k: int = 4):
  all_results = []
  seen_contents = set() # For deduplication
  
  for query in queries:
    print(f"🔍 Searching with: {query}")
    results = vector_db.similarity_search(
      query=query,
      k=top_k
    )
    
  # Deduplicate based on retrieved chunk content

  for result in results:
    content_hash = hash(result.page_content)
    
    if content_hash not in seen_contents:
      seen_contents.add(content_hash)
      all_results.append(result)
      
  return all_results    

# Main Rag Flow

question = input("Type your question here: ")

print("\n Generating query variations...")
parallel_queries = generate_parallel_queries(question)

print("\n Query variations:")
for i,q in enumerate(parallel_queries, 1):
  print(f" {i}. {q} ")
  
print("\n Retrieving documents...")  

search_results = retrieve_with_parallel_queries(parallel_queries, top_k=3)

print(f"\n✅ Retrieved {len(search_results)} unique documents\n")

context = "\n\n---\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

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