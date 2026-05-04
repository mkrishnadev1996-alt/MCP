
import asyncio
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

async def main():
    print("Hello from mcp-check!")

    # LLM test
    # print(llm.invoke("Hello world").content)

    # MCP client
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "C:/Users/VamsiAD/Dev/AI/MCP-check/servers/math_server.py"
                ],
                "transport": "stdio",
            }
            ,
        "weather": {
            # Make sure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable-http",
        }
        }
    )

    # Load MCP tools
    tools = await client.get_tools()

    print(f"Loaded {len(tools)} tools")

    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools
    )

    # Math request
    math_response = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(content="what's (3 + 5) x 12?")
            ]
        }
    )

    print("\nMath Response:")
    print(math_response)

    # Weather request
    weather_response = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(content="what is the weather in NYC?")
            ]
        }
    )

    print("\nWeather Response:")
    print(weather_response)

if __name__ == "__main__":
    asyncio.run(main())
