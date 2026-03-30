from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

COLLECTION_NAME = "learning_vectors"

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

question = input("Type your question here: ")

search_results = vector_db.similarity_search(
  query=question
)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
  You are an helpful AI Assistant who answers users query based on the available context retrieved.
  
  You should only answer the user based on the following context and navigate the user to open the right page number to know more. If you don't get the answer from the available context for the user question then let the user know that you don't know the answer of the user question.
  
  Context: {context}
"""

chat_completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
)

print(f"🤖: {chat_completion.choices[0].message.content}")