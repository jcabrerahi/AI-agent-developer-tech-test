from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any
from langchain_core.documents import Document

class VectorDBRepository(ABC):
    """Interface for vector database repositories."""
    
    @abstractmethod
    def similarity_search(self, query: str, k: int = 3) -> List[Document]:
        """Search for documents similar to the query."""
        pass
    
    @abstractmethod
    def similarity_search_with_score(self, query: str, k: int = 3, filter: Dict[str, Any] = None) -> List[Tuple[Document, float]]:
        """Search for documents similar to the query and return the score."""
        pass
    
    @abstractmethod
    def store_documents(self, documents: List[Document], persist_directory: str, collection_name: str) -> None:
        """Store documents in the vector database."""
        pass