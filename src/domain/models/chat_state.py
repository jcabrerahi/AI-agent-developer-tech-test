from typing_extensions import List, TypedDict
from typing import Annotated, Sequence
from langchain_core.messages import BaseMessage

from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages] 
    question: str = None
    context: str = None
    answer: str = None