from dotenv import load_dotenv

load_dotenv()

import os
from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from src.domain.repositories.vector_db_repository import VectorDBRepository
from src.infrastructure.vectorstore.chroma_repository import ChromaRepository


class VectorSearchService:
    """Service for vector search."""

    def __init__(self, repository: VectorDBRepository):
        self.repository = repository

    def search_documents(self, query: str, k: int = 3) -> list[Document]:
        """Search for documents similar to the query."""
        return self.repository.similarity_search(query, k=k)

    def search_documents_with_score(
        self, query: str, k: int = 3, filters: dict[str, Any] | None = None
    ) -> list[tuple[Document, float]]:
        """Search for documents similar to the query and return the score."""
        return self.repository.similarity_search_with_score(query, k=k, filters=filters)


def create_vector_search_service() -> VectorSearchService:
    """Initialize and return the vector search service."""

    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    persist_dir = base_dir / "data" / "chroma_db_2"

    persist_dir_str = str(persist_dir)

    embedding_model = os.getenv("EMBEDDING_MODEL")

    repository = ChromaRepository(
        persist_directory=persist_dir_str,
        collection_name="tax_policies",
        embedding_function=OpenAIEmbeddings(model=embedding_model, dimensions=512, max_retries=2, request_timeout=4),
    )

    return VectorSearchService(repository)
