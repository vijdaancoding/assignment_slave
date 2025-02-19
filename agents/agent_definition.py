import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    api_key=api_key
)