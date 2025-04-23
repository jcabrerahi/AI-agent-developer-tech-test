from typing import Any

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from src.domain.repositories.vector_db_repository import VectorDBRepository


class ChromaRepository(VectorDBRepository):
    """Implement the VectorDBRepository interface using Chroma."""

    def __init__(
        self,
        persist_directory: str = "./chroma_db",
        collection_name: str = "tax_policies",
        embedding_function: OpenAIEmbeddings = OpenAIEmbeddings(),
    ):
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.embedding_function = embedding_function

    def _get_db(self) -> Chroma:
        """Obtain the Chroma database instance."""
        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_function,
            collection_name=self.collection_name,
        )

    def similarity_search(self, query: str, k: int = 3) -> list[Document]:
        """Search for documents similar to the query."""
        db = self._get_db()
        return db.similarity_search(query, k=k)

    def similarity_search_with_score(
        self, query: str, k: int = 3, filter: dict[str, Any] | None = None
    ) -> list[tuple[Document, float]]:
        """Search for documents similar to the query and return the score."""
        db = self._get_db()
        return db.similarity_search_with_score(query, k=k, filter=filter)

    def store_documents(self, documents: list[Document], persist_directory: str, collection_name: str) -> None:
        """Store documents in the vector database."""
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_function,
            persist_directory=persist_directory,
            collection_name=collection_name,
        )
