from langchain_ollama import ChatOllama

llm  = ChatOllama(
    model="gemma4:12b",
    base_url="http://localhost:11500"
)

response = llm.invoke("are you connected?")

print(response.content)