from ollama import chat
from config import MODEL_NAME

def build_prompt(question: str, docs: str) -> str:
    return (
        f"You are a helpful assistant.\n"
        f"User question: {question}\n"
        f"Retrieved content from slides:\n{docs}\n"
        f"Please provide a concise, informative answer based only on this context."
    )

def run_chat(prompt: str):
    return chat(
        model=MODEL_NAME,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )
