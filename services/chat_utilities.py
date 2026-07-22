import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from llama_index.core.llms import MessageRole , ChatMessage
from llm_factory.get_llm import get_ollama_llm

def get_answer(model_name, chat_history):
    llm = get_ollama_llm(model_name)

    # Always prepend a system message
    messages = [
        ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful chat assistant.")
    ]

    # Append the rest of the history
    messages.extend(
        ChatMessage(role=MessageRole[msg["role"].upper()], content=msg["content"])
        for msg in chat_history
    )

    response = llm.chat(messages=messages)
    return response.message.content


# example usage
# model_name = "gemma2:2b"
# chat_history = [
#     {"role": "user", "content": "What is Artificial Intelligence?"}
# ]
# response = get_answer(model_name, chat_history)
# print(response)