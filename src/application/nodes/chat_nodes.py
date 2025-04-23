from langchain_core.messages import AIMessage
from src.domain.models.chat_state import ChatState
from src.infrastructure.tools.chat_qa_tool import ChatQATool
from langchain_core.messages import AIMessage

def chat_node(state: ChatState) -> ChatState:
    user_input = state["question"].content
    context = state["context"]    
    rendered_messages = "\n".join([f"{message.type}:{message.content}" for message in state["messages"]])

    tool_input = {
        "context": context,
        "question": user_input,
        "messages": rendered_messages,
    }
    tool_output = ChatQATool().run(tool_input)

    state["messages"].append(AIMessage(content=tool_output))
    state["answer"] = tool_output
    return state