from typing import List, Tuple, Dict, Any
from langchain_core.documents import Document

from src.domain.repositories.vector_db_repository import VectorDBRepository

class VectorSearchService:
    """Service for vector search."""
    
    def __init__(self, repository: VectorDBRepository):
        self.repository = repository
    
    def search_documents(self, query: str, k: int = 3) -> List[Document]:
        """Search for documents similar to the query."""
        return self.repository.similarity_search(query, k=k)
    
    def search_documents_with_score(self, query: str, k: int = 3, filter: Dict[str, Any] = None) -> List[Tuple[Document, float]]:
        """Search for documents similar to the query and return the score."""        
        return self.repository.similarity_search_with_score(query, k=k, filter=filter)