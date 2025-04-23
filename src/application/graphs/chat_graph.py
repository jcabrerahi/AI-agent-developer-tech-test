from langchain_openai.chat_models import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
# from langgraph.checkpoint.sqlite import SqliteSaver
# import sqlite3
from langgraph.graph import START, END, StateGraph

from src.domain.models.chat_state import ChatState
from src.application.nodes.chat_nodes import chat_node
from src.application.nodes.rag_nodes import retrieve_documents_node


llm = ChatOpenAI(model="gpt-4o-mini", streaming=True, temperature=0)
memory = MemorySaver()

# conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
# memory = SqliteSaver(conn)

workflow = StateGraph(ChatState)

# Add nodes
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("chat_qa", chat_node)

# Define workflow
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "chat_qa")

chat_graph = workflow.compile(checkpointer=memory)
