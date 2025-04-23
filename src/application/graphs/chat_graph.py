from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langgraph.graph import START, END, StateGraph

from src.domain.models.chat_state import ChatState
from src.application.nodes.chat_nodes import chat_node
from src.application.nodes.rag_nodes import retrieve_documents_node

conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
memory = SqliteSaver(conn)

workflow = StateGraph(ChatState)

# Add nodes
workflow.add_node("retrieve_rag", retrieve_documents_node)
workflow.add_node("chat_qa", chat_node)

# Define workflow
workflow.add_edge(START, "retrieve_rag")
workflow.add_edge("retrieve_rag", "chat_qa")
workflow.add_edge("chat_qa", END)

chat_graph = workflow.compile(checkpointer=memory)

try:    
    print("Langraph tax policies graph:")
    # print(chat_graph.get_graph().draw_mermaid()) 
    # print(chat_graph.get_graph(xray=True).draw_ascii())
except:
    print("Could not draw graph")
    