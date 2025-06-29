from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider

auth = BearerAuthProvider(
    jwks_uri="https://dev-yhz8yeukzpatil6h.us.auth0.com/.well-known/jwks.json",
    issuer="https://dev-yhz8yeukzpatil6h.us.auth0.com/",
    audience="mcp-api"
)


mcp = FastMCP("Streamable-server",stateless_http=True,auth=auth)


@mcp.tool(description="add two numbers")
def add(a:int, b:int)->int:
   """
   Add two numbers
   """
   return a + b
    

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    