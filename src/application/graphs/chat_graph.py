from dotenv import load_dotenv

load_dotenv()

from langchain_openai.chat_models import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, END, StateGraph

from src.domain.models.chat_state import ChatState
from src.application.nodes.chat_nodes import chat_node


llm = ChatOpenAI(model="gpt-4o-mini", streaming=True, temperature=0)
memory = MemorySaver()


workflow = StateGraph(ChatState)

# Add nodes
workflow.add_node("chat_qa", chat_node)

# Define workflow
workflow.add_edge(START, "chat_qa")

chat_graph = workflow.compile(checkpointer=memory)
