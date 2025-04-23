from src.domain.models.chat_state import ChatState
from src.infrastructure.tools.chat_qa_tool import ChatQATool


def chat_node(state: ChatState) -> ChatState:
    user_input = state["question"]
    context = state["context"]
    state["messages"].append(("User", user_input))

    if True:
        tool_input = {
            "context": context,
            "question": user_input,      
        }
        tool_output = ChatQATool().run(tool_input)
    else:
        tool_output = "Try it again please!"

    state["messages"].append(("AI", tool_output))
    state["answer"] = state["messages"][-1]
    return state