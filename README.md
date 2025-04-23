# AI-agent-developer-tech-test
Este proyecto es una prueba técnica que implementa un agente de chat con capacidades de RAG (Retrieval Augmented Generation) utilizando tecnologías modernas de procesamiento de lenguaje natural. The project follows a Clean Architecture and a hybrid Hexagonal Architecture, ensuring that the code is easily scalable and maintainable.

## Ejemplos de implementación
En la siguiente imagen se interactua con el chatbot preguntando inforamción de impuestos se cierra el chatbot y se vuelve a iniciar. Notando que el chatbot recuerda el contexto de la conversación anterior.
<img src="static/interaction_long_term_memory.jpg" alt="Chat Graph" width="1000"/>

Y en la siguiente imagen otro ejemplo de la interacción con el chatbot.
<img src="static/interaction_taxes.jpg" alt="Chat Graph" width="400"/>


## Tecnologías Utilizadas
- LangChain : Framework para desarrollo de aplicaciones con LLMs
- LangGraph : Biblioteca para crear flujos de trabajo con LLMs
- ChromaDB : Base de datos vectorial para almacenamiento local de embeddings
- SQLite : Base de datos relacional para persistencia de mensajes del chat
- Rich : Biblioteca para interfaces CLI mejoradas
- OpenAI : Integración con modelos de lenguaje avanzados
- Pydantic : Validación de datos y esquemas
- Python : Lenguaje de programación base
## Estructura del Proyecto
The project follows Clean Architecture and a hybrid of Hexagonal Architecture, which helps the code evolve easily. The directory structure is as follows:
```plaintext
AI-agent-developer-tech-test/
├── LICENSE                      # License file for the project
├── Makefile                     # Automates common project tasks
├── README.md                    # Project documentation
├── data/
│   ├── chroma_db_2/             # ChromaDB vector database
│   └── local_tax_policies.csv   # Sample data for local tax policies
├── poetry.lock                  # Poetry lock file for dependency versions
├── pyproject.toml               # Defines dependencies with Poetry
├── requirements.txt             # Lists project dependencies for installation
├── src/
│   ├── __init__.py              # Initializes the `src` package
│   ├── application/
│   │   ├── __init__.py          # Initializes the `application` package
│   │   ├── dto/                 # Data Transfer Objects
│   │   ├── graphs/              # Defines LangGraph workflows
│   │   │   ├── __init__.py
│   │   │   └── chat_graph.py    # Main chat graph definition
│   │   ├── nodes/               # Nodes for the workflow
│   │   │   ├── __init__.py
│   │   │   ├── chat_nodes.py    # Node for handling user queries and responses
│   │   │   └── rag_nodes.py     # Node for retrieving documents from the vector database
│   │   ├── prompts/             # Prompt templates for the chatbot
│   │   │   └── chat_prompts.py
│   │   └── services/            # Application services
│   │       ├── vector_ingest_service.py  # Service for ingesting documents into the vector database
│   │       └── vector_search_service.py  # Service for searching relevant documents in the vector database
│   ├── core/
│   │   ├── __init__.py          # Initializes the `core` package
│   │   ├── logging.py           # Logging configuration
│   │   └── settings.py          # Application settings
│   ├── domain/
│   │   ├── __init__.py          # Initializes the `domain` package
│   │   ├── models/              # Domain models
│   │   │   ├── __init__.py
│   │   │   └── chat_state.py    # Defines the state model for the chat
│   │   ├── repositories/       # Repositories for interacting with the vector database
│   │   │   ├── __init__.py
│   │   │   └── vector_db_repository.py  # Interface for vector DB interaction
│   │   └── services/            # Domain services
│   │       └── __init__.py
│   ├── infrastructure/          # Infrastructure code
│   │   ├── __init__.py          # Initializes the `infrastructure` package
│   │   ├── llm/                 # Wrappers for language models
│   │   │   └── openai_wrapper.py  # Wrapper for OpenAI API
│   │   ├── tools/               # Custom tools
│   │   │   ├── __init__.py
│   │   │   └── chat_qa_tool.py  # Tool for answering questions using LangChain BaseTool
│   │   └── vectorstore/         # Code for managing the vector database
│   │       ├── __init__.py
│   │       └── chroma_repository.py  # ChromaDB repository implementation
│   └── setup/                   # Setup and initialization scripts
│       ├── __init__.py
│       ├── ingest_vectorstore.py  # Script to load data into the vector store
│       └── init_all.py          # Initializes all components of the system
├── static/                    # Static assets for documentation
└── tests/
    ├── __init__.py
    ├── conftest.py             # Test configurations
    └── integration/            # Integration tests
        ├── __init__.py
        └── test_graphs.py      # Unit and integration tests for test the created langgraphs
 ```


## Características Principales
### RAG con ChromaDB
El sistema implementa un mecanismo de RAG (Retrieval Augmented Generation) utilizando ChromaDB como base de datos vectorial local. Esto permite:

- Almacenamiento eficiente de embeddings
- Búsqueda semántica de documentos relevantes
- Recuperación de contexto para mejorar las respuestas del LLM
### Memoria Persistente con SQLite
La aplicación utiliza SQLite para proporcionar persistencia de mensajes a largo plazo, permitiendo:

- Almacenamiento de conversaciones completas
- Recuperación del historial de chat
- Contexto conversacional entre sesiones
### Flujo de Trabajo con LangGraph
El sistema implementa un flujo de trabajo usando LangGraph que consta de los siguientes nodos:

1. __start__ : Punto de entrada al grafo
2. retrieve_rag : Recupera documentos relevantes basados en la consulta del usuario
3. chat_qa : Genera respuestas utilizando el contexto recuperado
4. __end__ : Punto de salida del grafo
### Herramientas Personalizadas
El proyecto utiliza herramientas personalizadas creadas mediante la subclase BaseTool de LangChain, lo que proporciona:

- Mayor versatilidad en la implementación
- Integración fluida con el ecosistema LangChain
- Capacidad para extender funcionalidades fácilmente

### Interfaz CLI con Rich
La aplicación utiliza Rich para crear una interfaz de línea de comandos mejorada con:

- Formato de texto enriquecido
- Mejor experiencia de usuario en terminal
- Visualización clara de la información
## Implementación del Grafo
El proyecto implementa un grafo de flujo de trabajo utilizando LangGraph, como se muestra en la imagen adjunta:

<img src="static/chat_graph.jpg" alt="Chat Graph" width="200"/>

Este flujo permite:

1. Iniciar la conversación
2. Recuperar documentos relevantes basados en la consulta del usuario
3. Generar respuestas contextualizadas
4. Finalizar el proceso

## Getting Started (Setup project)
To run this project, follow these detailed steps:

### 1. Clone the repository
First, clone the repository to your local machine:

```
git clone https://github.com/your_username/ai-agent-developer-tech-test.git
cd ai-agent-developer-tech-test
```
### 2. Install dependencies with Poetry
This project uses Poetry for dependency management. If you don't have Poetry installed, you can do so by running the following command:

Install Poetry:
If you don't have Poetry installed, you can install it by running:

```
curl -sSL https://install.python-poetry.org | python3 -
```
Once Poetry is installed, navigate to the project folder and run:

```
poetry install
```
This will install all the necessary dependencies defined in the pyproject.toml file.

### 3. Configure environment variables
The project requires some environment variables to work correctly, especially those related to OpenAI integration.

Create a .env file in the root of the project and add the following variables:

```
OPENAI_API_KEY=your_openai_api_key
EMBEDDING_MODEL=text-embedding-ada-002  # or the model you're using
```
Be sure to replace your_openai_api_key with your actual OpenAI API key.

### 4. Activate the virtual environment with Poetry
To activate the virtual environment managed by Poetry, run:

```
poetry shell
```
This will activate the virtual environment, and you can run the project commands within this isolated environment.

### 5. Running the application
Once the virtual environment is activated, you can run the application using the following command:

```
python -m src.application
```
This will start the application, and you can interact with the chatbot.

### 6. Running Tests (Optional)
To run the tests, use the Makefile commands. This will execute the tests defined in the tests/ folder:

```
make run
```
This will execute the following command:

```
python -m tests.unit.test_graphs
```
### 7. Populate the vector store (Optional)
If you'd like to recreate the vector store (which is already included in the repository), you can use the following command from the Makefile to populate it:
```
make populate_vector_store
```
This will execute the following command:

```
python -m src.setup.ingest_vectorstore
```
However, note that the vector store already exists in the repository as data/chroma_db_2, so this step is not necessary unless you want to recreate it.

## Contribuciones
Este proyecto es una prueba técnica y no está abierto a contribuciones externas.

## Licencia
Derechos reservados.