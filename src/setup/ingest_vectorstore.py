import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

from src.application.services.vector_ingest_service import VectorIngestService
from src.application.services.vector_search_service import VectorSearchService
from src.infrastructure.vectorstore.chroma_repository import ChromaRepository

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    if not os.getenv("EMBEDDING_MODEL"):
        raise ValueError("EMBEDDING_MODEL not found in environment variables")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    base_dir = Path(__file__).parent.parent.parent
    csv_path = base_dir / "data" / "local_tax_policies.csv"
    persist_dir = base_dir / "data" / "chroma_db_2"

    # Convertir el objeto Path a string para evitar el error de tipo
    persist_dir_str = str(persist_dir)

    repository = ChromaRepository(
        persist_directory=persist_dir_str,
        collection_name="tax_policies",
        embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL, dimensions=512, max_retries=2, request_timeout=4),
    )

    ingest_service = VectorIngestService(repository)

    # Pasar la ruta como string
    ingest_service.ingest_from_csv(str(csv_path), persist_dir_str)

    search_service = VectorSearchService(repository)
    query = "What is the property tax rate in Travis County?"
    results = search_service.search_documents_with_score(query, k=5)

    for _doc, _score in results:
        pass
