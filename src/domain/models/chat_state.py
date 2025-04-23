from typing_extensions import List, TypedDict

class ChatState(TypedDict):
    question: str
    context: str
    answer: str
    messages: List[str]