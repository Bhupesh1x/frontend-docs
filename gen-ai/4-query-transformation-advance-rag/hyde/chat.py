import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTION_NAME = "learning_vectors_with_hyde"

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

def generate_hypothetical_document(query: str):
  
  prompt = f"""
    Generate a detailed, technical answer to this question as if you were writing a documentation:
    
    Question: {query}
    
    Write a detailed answer (3-4 paragraphs) that includes:
    - Technical terminology and concepts
    - Related terms and jargons
    - Detailed explanations
    - Specific examples or methods
    
    This is for search purposes, so be thorough and use precise language.
  """
  
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
  )
  
  return response.choices[0].message.content.strip()


def search_with_hyde(doc: str, k: int = 6):
  results = vector_db.similarity_search(query=doc, k=k)
  return results

# Main Rag Flow

question = input("Type your question here: ")

print("\n Generating hypothetical document...")
doc = generate_hypothetical_document(question)

print(f"\n📄 Hypothetical Document (first 200 chars):")
print(f"   {doc[:200]}...")
print(f"   [Total length: {len(doc)} characters]")
  
print("\n Searching with hypothetical document...")  

search_results = search_with_hyde(doc=doc)
      
print(f"✅ Retrieved {len(search_results)} documents\n")
      
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