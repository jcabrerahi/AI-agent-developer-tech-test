import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

from src.application.services.vector_ingest_service import VectorIngestService
from src.application.services.vector_search_service import VectorSearchService
from src.infrastructure.vectorstore.chroma_repository import ChromaRepository

load_dotenv()

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    if not os.getenv("EMBEDDING_MODEL"):
        raise ValueError("EMBEDDING_MODEL not found in environment variables")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    csv_path = os.path.join(base_dir, "data", "local_tax_policies.csv")
    persist_dir = os.path.join(base_dir, "data", "chroma_db_2")


    repository = ChromaRepository(
        persist_directory=persist_dir,
        collection_name="tax_policies",
        embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL, dimensions=512, max_retries=2, request_timeout=4),
    )

    ingest_service = VectorIngestService(repository)

    ingest_service.ingest_from_csv(csv_path, persist_dir)

    search_service = VectorSearchService(repository)
    query = "What is the property tax rate in Travis County?"
    results = search_service.search_documents_with_score(query, k=5)

    for _doc, _score in results:
        pass

