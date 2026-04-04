import os

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTION_NAME = "learning_vectors_with_model_routing"

MODELS = {
  "simple": "gpt-4o-mini",
  "medium": "gpt-4o",
  "medium": "gpt-4.1",
}

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


def classify_query_complexity(user_query: str):
  prompt = f"""
    Please classify this query's complexity into ONE category:
    
    SIMPLE: Straightforward questions, definitions, basic facts
    - Examples: "What is X?", "List the steps", "Explain Y briefly"
    
    MEDIUM: Moderate analysis, comparisons,  multi-step reasoning
    - Examples: "Compare X vs Y", "How does Z work?", "Refactor this code"
    
    COMPLEX: Deep analysis, system design, complex reasoning, creative tasks
    - Examples: "Design a distributed system", "Analyze trade-offs", "Create comprehensive plan"
    
    Query: {user_query}
    
    Return only one word: simple, medium or complex
  """
  
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
  )
  
  complexity = response.choices[0].message.content.strip().lower()
  
  if complexity in MODELS:
    return complexity
  else:
    return "medium"
  
def get_model_for_complexity(complexity: str):
    return MODELS.get(complexity, MODELS["medium"])    

# Main Rag Flow

question = input("Type your question here: ")

print("\n Analyzing query complexity...")
complexity = classify_query_complexity(question)
selected_model = get_model_for_complexity(complexity)

print(f"Complexity: {complexity.upper()}")
print(f"Selected model: {selected_model}")
  
print("\n Searching vector database...")  

search_results = vector_db.similarity_search(query=question, k=5)
      
print(f"✅ Retrieved {len(search_results)} documents\n")
      
context = "\n\n---\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
  You are an helpful AI Assistant who answers users query based on the available context retrieved.
  
  You should only answer the user based on the following context and navigate the user to open the right page number to know more. If you don't get the answer from the available context for the user question then let the user know that you don't know the answer of the user question.
  
  Context: {context}
"""

print("Generating answer...")
chat_completion = client.chat.completions.create(
    model=selected_model, # Use routed model
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
)

print(f"🤖: {chat_completion.choices[0].message.content}")