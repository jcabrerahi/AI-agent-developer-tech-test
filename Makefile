run:
	python -m src.application.use_cases.call_graph

test:
	poetry run pytest tests/integration/test_graphs.py

populate_vector_store:
	python -m src.setup.ingest_vectorstore

format:
	poetry run ruff format --config ./tools/linters/ruff.toml

lint:
	poetry run ruff check . --extend-select I --fix --config ./tools/linters/ruff.toml