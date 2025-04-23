from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver 
from langchain_core.tools import tool
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Define state structure
class State(TypedDict):
    messages: list
    human_input: str

# Define the StateGraph
graph_builder = StateGraph(State)

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")

# Example magic function tool
@tool
def magic_function(input: int) -> int:
    """Applies a magic function to an input."""
    return input + 2

tools = [magic_function]

# Initialize the OpenAI model
model = ChatOpenAI(model="gpt-4o", api_key=OPEN_AI_API_KEY)

# Configuration for the chat
config = {"configurable": {"thread_id": "test-thread"}}

from langgraph.checkpoint.memory import MemorySaver  # an in-memory checkpointer
from langgraph.prebuilt import create_react_agent

system_message = "You are a helpful assistant."

memory = MemorySaver()
langgraph_agent_executor = create_react_agent(
    model, tools, prompt=system_message, checkpointer=memory
)

print(
    langgraph_agent_executor.invoke(
        {
            "messages": [
                ("user", "Hi, I'm polly! What's the output of magic_function of 3?")
            ]
        },
        config,
    )["messages"][-1].content
)
print("---")
print(langgraph_agent_executor)
print(
    langgraph_agent_executor.invoke(
        {"messages": [("user", "Remember my name?")]}, config
    )["messages"][-1].content
)
print("---")
print(
    langgraph_agent_executor.invoke(
        {"messages": [("user", "what was that output again?")]}, config
    )["messages"][-1].content
)