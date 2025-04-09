from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
import asyncio
import os
import sys
import traceback
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(
    model="qwen-2.5-32b",
    temperature=0.3,
    max_tokens=1024
)

current_dir = os.path.dirname(os.path.abspath(__file__))
server_file = os.path.join(current_dir, "server.py")

server_params = StdioServerParameters(
    command=sys.executable,
    args=[server_file],
    cwd=current_dir,
    env=os.environ.copy(),
)

async def test_tools_directly():
    print("Testing tools directly...")
    try:
        async with stdio_client(server_params) as (read, write):
            print("Connected to server...")
            
            async with ClientSession(read, write) as session:
                print("Session created, initializing...")
                await session.initialize()
                print("Session initialized, loading tools...")
                
                tools = await load_mcp_tools(session)
                print(f"Tools loaded: {[tool.name for tool in tools]}")

                search_tool = next((tool for tool in tools if tool.name == "search"), None)
                if not search_tool:
                    return "Search tool not found"

                print("Executing search tool...")
                try:
                    result = await search_tool.ainvoke({"query": "Who is the president of india?"})
                    print("Search tool executed successfully")
                    return f"Direct tool result: {result}"
                except Exception as e:
                    print(f"Error invoking search tool: {e}")
                    traceback.print_exc()
                    return f"Error invoking search tool: {str(e)}"
    except Exception as e:
        print(f"Error in test_tools_directly: {e}")
        traceback.print_exc()
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("Starting DuckDuckGo search client...")
    try:
        print("\n--- Testing Tools Directly (No Agent) ---")
        direct_result = asyncio.run(test_tools_directly())
        print("\nDirect tool test result:")
        print(direct_result)
        
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred in the main execution: {str(e)}")
        traceback.print_exc()