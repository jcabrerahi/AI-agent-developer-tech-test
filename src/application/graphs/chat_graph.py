from langchain_openai.chat_models import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
# from langgraph.checkpoint.sqlite import SqliteSaver
# import sqlite3
from langgraph.graph import START, END, StateGraph, MessagesState

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
workflow.add_edge("chat_qa", END)

chat_graph = workflow.compile(checkpointer=memory)

# try:
#     chat_graph.get_graph(xray=True).draw_mermaid_png(output_file_path="chat_graph.png")
#     print("Graph drawn")
# except:
#     print("Could not draw graph")
    