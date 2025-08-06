from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


async def run_agent():
   client = MultiServerMCPClient(
       {
           "DragonFileSystem": {
               "command": "python",
               "args": [
                   "./mcp_filesystem_server.py"
               ],
               "transport":"stdio"
           }

       }
   )
   tools = await client.get_tools()
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   response = await agent.ainvoke({"messages": "delete the file dragon.txt"})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())