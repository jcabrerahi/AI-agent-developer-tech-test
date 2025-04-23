import pprint
from rich.console import Console
from src.application.graphs.chat_graph import chat_graph

def chat_session():
    # Initialize the console for rich text output
    console = Console()
    
    config = {"configurable": {"thread_id": "1"}}
    
    console.print("\n===== Local Tax Policies Chatbot =====", style="bold green")
    console.print("Type 'exit' to end the conversation\n", style="italic yellow")
                         
    while True:        
        user_input = console.input("[bold blue]You: [/bold blue]")
        
        if user_input.lower() == 'exit':
            console.print("\nGoodbye!", style="bold red")
            break
                
        conversation_state = {
            "messages": [
                ("user", user_input)
            ]
        }
                
        final_output = None
        for output in chat_graph.stream(conversation_state, config, stream_mode="updates"):
            final_output = output
                    
        if final_output and 'chat_qa' in final_output:
            conversation_state = final_output['chat_qa']
            
            if isinstance(conversation_state['answer'], tuple) and len(conversation_state['answer']) > 1:
                console.print(f"\n[bold green]Chatbot:[/bold green] {conversation_state['answer'][1]}\n", style="white")
            else:
                console.print(f"\n[bold green]Chatbot:[/bold green] {conversation_state['answer']}\n", style="white")


if __name__ == "__main__":
    chat_session()