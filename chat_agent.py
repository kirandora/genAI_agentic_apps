from dotenv import load_dotenv

load_dotenv()

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
   model="groq:llama-3.3-70b-versatile", 
   tools=[get_weather], 
   checkpointer=checkpointer 
)


# Run the agent
config = {"configurable": {"thread_id": "1"}}
response = agent.invoke(
   {"messages": [{"role": "user", "content": "who is modi?"}]}, config
)

print(response["messages"][-1].content)

response = agent.invoke(
   {"messages": [{"role": "user", "content": "when he was born?"}]}, config
)

print(response["messages"][-1].content)


# code to create the graph
try:
   img = agent.get_graph().draw_mermaid_png()
   with open("graph.png", "wb") as f:
       f.write(img)
except Exception:
   pass






