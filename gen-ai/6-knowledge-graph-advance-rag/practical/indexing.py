import os

from dotenv import load_dotenv

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.graphs import Neo4jGraph

load_dotenv()

COLLECTION_NAME = "kg_rag_langchain"

# Neo4j connection — LangChain handles the driver internally
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
)

llm = ChatOpenAI(model="gpt-4o-mini")
graph_transformer = LLMGraphTransformer(llm=llm)

qdrant_url = os.getenv("QDRANT_URL")

pdf_path = Path(__file__).parent / "nodejs.pdf"

# Loading
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()  # Read PDF File

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

split_docs = text_splitter.split_documents(documents=docs)

# Extract graph from chunks & store in Neo4j — one line!
graph_docs = graph_transformer.convert_to_graph_documents(split_docs)
graph.add_graph_documents(graph_docs, include_source=True)

# Vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Using [embedding_model] create embeddings of [split_docs] and store in DB using langchain utility
vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url=qdrant_url,
    collection_name=COLLECTION_NAME,
    embedding=embedding_model
)

print("Indexing of Documents Done...")