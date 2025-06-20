from fastmcp import FastMCP


mcp = FastMCP("Streamable-server",stateless_http=True)


@mcp.tool(description="add two numbers")
def add(a:int, b:int)->int:
   """
   Add two numbers
   """
   return a + b
    

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    