from fastmcp import FastMCP
# from tavily import TavilyClient
# from dotenv import load_dotenv
from typing import List, Dict
import os


# API related setup
# load_dotenv()

# if "TAVILY_API_KEY" not in os.environ:
#     raise Exception("TAVILY_API_KEY is not set")

# tavily_api_key = os.getenv("TAVILY_API_KEY")
# tavily_client = TavilyClient(tavily_api_key)

PORT = os.environ.get("PORT", 10000)
# initialize the mcp server
mcp = FastMCP("Add two numbers", host="0.0.0.0", port=PORT)


# define the web search tool
@mcp.tool(description="add two numbers")
def add(a:int, b:int)->int:
    """
    Use this tool to add two numbers

    Args:
    a: The first number
    b: The second number

    Returns:
    the sum of the two numbers
    """
    try:
        return a + b
    except Exception as e:
        return f"Error adding the numbers: {e}"

    
# run the mcp server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    