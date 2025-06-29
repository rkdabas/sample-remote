from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import httpx, os

# Env vars (fill from Paytm developer console)
PAYTM_CLIENT_ID = os.environ["PAYTM_CLIENT_ID"]
PAYTM_CLIENT_SECRET = os.environ["PAYTM_CLIENT_SECRET"]
PAYTM_AUTH = "https://accounts.paytm.com/oauth2/authorize"
PAYTM_TOKEN = "https://accounts.paytm.com/oauth2/token"
REDIRECT_URI = "http://localhost:7736/oauth/callback"

# 1. Setup MCP server with BearerAuthProvider
auth = BearerAuthProvider(
    issuer="https://accounts.paytm.com",
    jwks_uri="https://accounts.paytm.com/.well-known/jwks.json",
    audience=PAYTM_CLIENT_ID,
    required_scopes=["read"],
)
mcp = FastMCP("Paytm-MCP", stateless_http=True, auth=auth)

@mcp.tool(description="add two numbers")
def add(a:int, b:int) -> int:
    return a + b

# 2. Callback handler for OAuth redirect
async def oauth_callback(request):
    params = dict(request.query_params)
    code = params.get("code")
    state = params.get("state")
    # Exchange for tokens
    resp = httpx.post(PAYTM_TOKEN, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":REDIRECT_URI,
        "client_id":PAYTM_CLIENT_ID,
        "client_secret":PAYTM_CLIENT_SECRET,
    })
    data = resp.json()
    access_token = data["access_token"]
    # return a simple HTML with script saving token into cursor
    return PlainTextResponse("Authorization successful! You may close this window and return to the CLI.")

# 3. Starlette app mounts MCP routes and callback
app = Starlette(routes=[
    Route("/oauth/callback", oauth_callback),
])
mcp.run(transport="streamable-http", app=app)
