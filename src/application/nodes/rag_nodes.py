from src.domain.models.chat_state import ChatState
from src.application.services.vector_search_service import create_vector_search_service


def retrieve_documents_node(state: ChatState) -> ChatState:
    """Node for retrieving relevant documents based on the user's question."""
    query = state["messages"][-1]
    state["question"] = query
        
    search_service = create_vector_search_service()            
    results = search_service.search_documents_with_score(query.content, k=3)
        
    context_parts = []
    
    for doc, score in results:
        context_parts.append(doc.page_content)        
       
    state["context"] = "\n".join(context_parts)
    
    return state
