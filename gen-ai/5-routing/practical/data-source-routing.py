import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTIONS = {
  "finance": "finance_collection",
  "hr": "hr_collection",
  "tech": "tech_collection",
  "operations": "operations_collection",
}

qdrant_url = os.getenv("QDRANT_URL")

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

def route_to_collection(user_query: str):
  prompt = f"""
    Classify this query into one of these categories:
    - finance (revenue, budget, costs, financial reports, expenses)
    - hr (policies, leave, reimbursement, benefits, onboarding)
    - tech (authentication, API, code, configuration, deployment)
    - finance (logistics, inventory, processes, workflows)
    
    Query: {user_query}
    
    Return only one of the relevant category name (finance/hr/tech/operations), nothing else. 
  """
  
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
  )
  
  category = response.choices[0].message.content.strip().lower()
  
  if category in COLLECTIONS:
    return COLLECTIONS[category]
  else:
    return COLLECTIONS["tech"]
  
def search_routed_collection(collection_name: str, query: str, k: int = 3):
  vector_db = QdrantVectorStore.from_existing_collection(
    url=qdrant_url,
    collection_name=collection_name,
    embedding=embedding_model
  )
    
  results = vector_db.similarity_search(query=query, k=k)
  return results  


# Main Rag Flow

question = input("Type your question here: ")

print("\n Routing to appropriate data source...")
selected_collection = route_to_collection(question)

print(f"Routed to: {selected_collection}")
  
print("\n Searching routed collection...")  

search_results = search_routed_collection(selected_collection, question, k=5)
      
print(f"\n Retrieved {len(search_results)} documents\n")
      
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