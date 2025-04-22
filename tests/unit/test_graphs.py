import pprint

from src.application.graphs.chat_graph import chat_graph

inputs = {
    "question": "What is the name of my friend?",
    "context": "My name is Julio and my friend is called Johnns, and also i'm a Data engineer from 5 years",
    "answer": "",    
    "messages": []
}

config = {"configurable": {"thread_id": "1"}}

for output in chat_graph.stream(inputs, config, stream_mode="updates"):
    for key, value in output.items():
        pprint.pprint(f"Output from node '{key}':")
        pprint.pprint("---")
        pprint.pprint(value, indent=2, width=80, depth=None)
    pprint.pprint("\n---\n")