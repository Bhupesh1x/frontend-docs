import os

from dotenv import load_dotenv

from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain

load_dotenv()

COLLECTION_NAME = "kg_rag_langchain"

qdrant_url = os.getenv("QDRANT_URL")

# Connect to Neo4j Knowledge Graph
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
)

# Connect to Qdrant Vector Database
vector_db = QdrantVectorStore.from_existing_collection(
    url=os.getenv("QDRANT_URL"),
    collection_name=COLLECTION_NAME,
    embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
)

# Initialized a retriever from the vector database
# This will search for the top 5 most similar document chunks
retriever = vector_db.as_retriever(search_kwargs={"k": 5})

llm = ChatOpenAI(model="gpt-4.1")

# Create a chain that can query the Neo4j graph using natural language
# This automatically converts questions to Cypher queries
graph_chain = GraphCypherQAChain.from_llm(llm=llm, graph=graph, verbose=True)

def get_vector_context(question):
  docs = retriever.invoke(question)
  return "\n\n---\n\n".join([f"[Page {d.metadata.get('page')}]\n{d.page_content}" for d in docs])

def get_graph_context(question):
  return graph_chain.invoke({"query": question})["result"]

def build_prompt(vector_context, graph_context, question):
  system_message = f"""You are a helpful AI Assistant. Answer the user's question using BOTH contexts provided below.

  Vector Context (relevant document chunks):
  {vector_context}

  Graph Context (relationships and facts):
  {graph_context}

  Instructions:
  - Combine information from both contexts to give a comprehensive answer
  - If the contexts conflict, explain the difference
  - If the contexts don't contain relevant information, say so
  - Cite which context you're using when appropriate
  """
  
  messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": question}
    ]
    
  return messages

def ask_question(question):
  # Step 1: Get relevant document chunks from vector database
    vector_context = get_vector_context(question)
    
    # Step 2: Get relevant facts/relationships from knowledge graph
    graph_context = get_graph_context(question)
    
    # Step 3: Build the complete prompt with both contexts
    messages = build_prompt(vector_context, graph_context, question)
    
    # Step 4: Send to the LLM and get response
    print("  🤖 Generating answer...")
    response = llm.invoke(messages)
    
    # Step 5: Extract and return just the text content
    return response.content


while True:
  # Get user input
  question = input("\n📝 Your Question: ").strip()
  
  # Check for exit commands
  if question.lower() in ['exit', 'quit', 'q']:
      print("\n👋 Goodbye!\n")
      break
  
  # Skip empty questions
  if not question:
      print("⚠️  Please enter a question.")
      continue
    
  try:
    answer = ask_question(question)
    print(f"\n🤖 Answer:\n{answer}")
    print("\n" + "=" * 70)
    
  except Exception as e:
    print(f"\n❌ Error occurred: {str(e)}")
    print("Please try again with a different question.\n")  