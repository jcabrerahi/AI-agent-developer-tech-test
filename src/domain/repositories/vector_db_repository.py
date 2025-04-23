from abc import ABC, abstractmethod
from typing import Any

from langchain_core.documents import Document


class VectorDBRepository(ABC):
    """Interface for vector database repositories."""

    @abstractmethod
    def similarity_search(self, query: str, k: int = 3) -> list[Document]:
        """Search for documents similar to the query."""

    @abstractmethod
    def similarity_search_with_score(
        self, query: str, k: int = 3, filter: dict[str, Any] | None = None
    ) -> list[tuple[Document, float]]:
        """Search for documents similar to the query and return the score."""

    @abstractmethod
    def store_documents(self, documents: list[Document], persist_directory: str, collection_name: str) -> None:
        """Store documents in the vector database."""
