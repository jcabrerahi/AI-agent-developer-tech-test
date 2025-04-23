import csv
import shutil
from pathlib import Path

from langchain_core.documents import Document

from src.domain.repositories.vector_db_repository import VectorDBRepository


class VectorIngestService:
    """Service for ingesting data into vector database."""

    def __init__(self, repository: VectorDBRepository):
        self.repository = repository

    def ingest_from_csv(
        self, csv_path: str, persist_directory: str = "./chroma_db", collection_name: str = "tax_policies"
    ) -> None:
        """Ingest data from CSV file into vector database."""
        if Path(persist_directory).exists():
            # ask if want to remove and recreate
            user_input = input(
                f"\n\nVector database already exists at {persist_directory}. Do you want to delete and recreate? (y/n) "
            )
            if user_input.lower() == "y":
                shutil.rmtree(persist_directory)

                documents = self._create_documents_from_csv(csv_path)

                self.repository.store_documents(documents, persist_directory, collection_name)

    def _create_documents_from_csv(self, csv_path: str) -> list[Document]:
        """Create documents from CSV file."""
        documents = []
        with Path(csv_path).open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                content = (
                    f"County: {row['county']}, State: {row['state']}, "
                    f"Property Tax Rate: {row['property_tax_rate']}, "
                    f"Sales Tax: {row['sales_tax']}, "
                    f"Local Income Tax: {row['income_tax_local']}, "
                    f"Notes: {row['notes']}"
                )

                metadata = {
                    "county": row["county"],
                    "state": row["state"],
                    "property_tax_rate": float(row["property_tax_rate"]),
                    "sales_tax": float(row["sales_tax"]),
                    "income_tax_local": float(row["income_tax_local"]),
                }

                documents.append(Document(page_content=content, metadata=metadata))

        return documents
