run:
	python -m tests.unit.test_graphs


populate_vector_store:
	python -m src.setup.ingest_vectorstore