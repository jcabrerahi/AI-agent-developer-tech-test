run:
	python -m src.application.use_cases.call_graph

test:
	poetry run pytest tests/integration/test_graphs.py

populate_vector_store:
	python -m src.setup.ingest_vectorstore