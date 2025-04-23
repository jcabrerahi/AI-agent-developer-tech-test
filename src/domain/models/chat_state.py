from typing import Annotated

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class ChatState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    question: str = None
    context: str = None
    answer: str = None
