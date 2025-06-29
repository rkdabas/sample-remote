from fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv
from typing import List, Dict
import os


# API related setup
load_dotenv()

if "TAVILY_API_KEY" not in os.environ:
    raise Exception("TAVILY_API_KEY is not set")

tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(tavily_api_key)


# initialize the mcp server
mcp = FastMCP("Web search", host="0.0.0.0", port=8000)


# define the web search tool
@mcp.tool(description="add two numbers")
def web_search(query:str)->List[Dict]:
    """
    Use this tool to search the web for the given query

    Args:
    query: The search query

    Returns:
    the search results
    """
    try:
        results = tavily_client.search(query)
        return results["results"]
    except Exception as e:
        return f"Error searching the web: {e}"

    
# run the mcp server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    