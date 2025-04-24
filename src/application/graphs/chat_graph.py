import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph

from src.application.nodes.chat_nodes import chat_node
from src.application.nodes.rag_nodes import retrieve_documents_node
from src.core.logging import logger
from src.domain.models.chat_state import ChatState

# Eliminar estas líneas
# conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
# memory = SqliteSaver(conn)

workflow = StateGraph(ChatState)

# Add nodes
workflow.add_node("retrieve_rag", retrieve_documents_node)
workflow.add_node("chat_qa", chat_node)

# Define workflow
workflow.add_edge(START, "retrieve_rag")
workflow.add_edge("retrieve_rag", "chat_qa")
workflow.add_edge("chat_qa", END)

# Eliminar el parámetro checkpointer
chat_graph = workflow.compile()

try:
    logger.info("Generating graph...")
    # logger.debug(chat_graph.get_graph().draw_mermaid())
    # logger.debug(chat_graph.get_graph(xray=True).draw_ascii())
except Exception:
    logger.error("Graph not generated")
