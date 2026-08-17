from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("GEMMA_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemma-4-31b-it", #"gemma-4-26b-a4b-it",          # or "gemma-4-31b-it"
    google_api_key=KEY,
    temperature=0.7
)

response  = llm.invoke("give 1 line answer - what you can do?")

print(response.content)