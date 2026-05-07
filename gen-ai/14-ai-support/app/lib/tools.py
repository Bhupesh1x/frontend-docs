from langchain.tools import tool

from .qdrant import createVectorStore

QUERY_LIMIT = 3

@tool
def search_tool(query: str) -> str:
  """
  Search the knowledge base for relevant information
  """
  
  vector_store = createVectorStore()
  
  results = vector_store.similarity_search_with_score(
    query=query,
    k=QUERY_LIMIT
  )  
  
  if not results:
    return "No Results Found"
  
  formatted_results = []
  
  for index, (doc, score) in enumerate(results):
    formatted_results.append(
      f"""
        RESULT: {index + 1}
        
        RELEVANCE SCORE: {score}
        
        CONTENT: {doc.page_content}
      """
    )

    return "\n\n---\n\n".join(formatted_results)
  
  
  
tools = [search_tool]  