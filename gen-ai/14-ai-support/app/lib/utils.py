from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def getPdfChunks(file_path):
  loader = PyPDFLoader(file_path)
  
  docs = loader.load()

  splitter = RecursiveCharacterTextSplitter(
      chunk_size=800,
      chunk_overlap=100
  )

  chunks = splitter.split_documents(docs)
  return chunks