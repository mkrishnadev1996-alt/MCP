import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")  #gemini-2.5-flash
async def main():
    print("Hello from mcp-check!")
    print(llm.invoke("Hello world"))


if __name__ == "__main__":
    asyncio.run(main())
