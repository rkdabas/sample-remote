from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair
from fastmcp.server.dependencies import get_access_token, AccessToken


# Generate a new key pair
key_pair = RSAKeyPair.generate()

auth = BearerAuthProvider(
    # jwks_uri="https://my-identity-provider.com/.well-known/jwks.json",
    public_key=key_pair.public_key,
    issuer="https://dev.example.com",
    audience="my-dev-server"
)

mcp = FastMCP("Streamable-server",stateless_http=True, auth=auth)

# Generate a token for testing
token = key_pair.create_token(
    subject="dev-user",
    issuer="https://dev.example.com",
    audience="my-dev-server",
    scopes=["read", "write"]
)

print(f"Test token: {token}")


@mcp.tool(description="add two numbers")
def add(a:int, b:int)->int:
   """
   Add two numbers
   """
   return a + b
    

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    