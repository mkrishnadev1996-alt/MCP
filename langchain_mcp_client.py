from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
import os
import asyncio

load_dotenv()

llm = ChatGoogleGenerativeAI(model = os.environ["GOOGLE_MODEL"]) 

async def main():
    server_params =StdioServerParameters(command="python",
                # Make sure to update to the full absolute path to your math_server.py file
                args= ["C:/Users/VamsiAD/Dev/AI/MCP-check/servers/math_server.py"]
    )
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
             # Initialize the connection
            await session.initialize()
            
            # Get tools
            tools = await load_mcp_tools(session)
            print(f"Tools = \n{tools}")

            # Create and run the agent inside session
            agent = create_agent(model=llm, tools=tools)
            math_response = await agent.ainvoke({"messages": [HumanMessage(content="what's (0 + 5) x (12 +6 ) * (10 - 2)?")]})
            print(math_response)
if __name__ == "__main__":
    asyncio.run(main=main())