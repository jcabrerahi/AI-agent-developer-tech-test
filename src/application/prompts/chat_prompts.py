from langchain.prompts import PromptTemplate

rag_prompt = """
    "Answer the following question based only on the provided context.\n\n"
    "Context: {context}\n"
    "Question: {question}"
"""