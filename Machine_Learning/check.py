import ollama

stream = ollama.chat(
    model="mistral:7b",
    messages=[{"role": "user", "content": "Generate code of traveling salesman"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
