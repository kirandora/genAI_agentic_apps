from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


async def run_agent():
   client = MultiServerMCPClient(
       {
           "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "/Users/kirandora/Desktop/BootCamp"
                ],
                "transport": "stdio"
            }
       }
   )
   tools = await client.get_tools()
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   response = await agent.ainvoke({"messages": "create the file sample.txt in directory /Users/kirandora/Desktop/BootCamp"})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())