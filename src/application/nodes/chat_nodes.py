from src.domain.models.chat_state import ChatState
from src.infrastructure.tools.chat_qa_tool import ChatQATool


def chat_node(state: ChatState) -> ChatState:
    user_input = state["question"].content
    context = state["context"]
    # state["messages"].append(("User", user_input))

    # Use the context from retrieved documents
    tool_input = {
        "context": context,
        "question": user_input,
        "messages": state["messages"],
    }
    tool_output = ChatQATool().run(tool_input)

    state["messages"] = [("ai", tool_output)]
    state["answer"] = tool_output
    return state