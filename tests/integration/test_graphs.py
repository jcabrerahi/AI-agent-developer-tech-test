import pytest

from src.application.graphs.chat_graph import chat_graph


@pytest.fixture
def conversation_state():
    # Initial state for the conversation
    return {"messages": [("user", "What are the property taxes for Orange?")]}


def test_chat_session(conversation_state):
    config = {"configurable": {"thread_id": "test123"}}

    final_output = None
    for output in chat_graph.stream(conversation_state, config, stream_mode="updates"):
        final_output = output

    assert final_output is not None
    assert "chat_qa" in final_output
    assert final_output["chat_qa"]["messages"][-1].content is not None
    assert "Orange" in final_output["chat_qa"]["messages"][-1].content
