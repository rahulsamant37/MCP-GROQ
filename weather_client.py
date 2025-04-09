from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio

server_params = StdioServerParameters(
  command="python",
  args=["weather.py"],  # Changed to match actual functionality
)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="qwen-2.5-32b")

async def run_agent():
  async with stdio_client(server_params) as (read, write):
    # Open an MCP session to interact with the tool server
    async with ClientSession(read, write) as session:
      # Initialize the session.
      await session.initialize()
      # Load tools
      tools = await load_mcp_tools(session)
      # Create a ReAct agent.
      agent = create_react_agent(model, tools)
      # Run the agent.
      agent_response = await agent.ainvoke(
        # Ask about tech news instead of weather
        {"messages": [{"role": "user", "content": "What's the latest news from arstechnica?"}]}
      )
      
      # Properly handle the response
      if "messages" in agent_response and len(agent_response["messages"]) > 0:
        # Return the last message in the conversation
        return agent_response["messages"][-1].content
      else:
        return "No response received from the agent"

if __name__ == "__main__":
  result = asyncio.run(run_agent())
  print(result)