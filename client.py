import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    url="http://127.0.0.1:8000/mcp", 
    headers={"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Rldi5leGFtcGxlLmNvbSIsInN1YiI6ImRldi11c2VyIiwiaWF0IjoxNzUwMzMzNTIxLCJleHAiOjE3NTAzMzcxMjEsImF1ZCI6Im15LWRldi1zZXJ2ZXIiLCJzY29wZSI6InJlYWQgd3JpdGUifQ.EIU8rN31QzUwuR6IKJgPpDS3lTyBfUoMg2X-i6s6Huwt8O1qSBTM-jI5ej0RAEOkqb34P3rQQq4_j4BoB-tHjGLc0zu1foTnbL37KnpHwX4LD0MG5lmfqUuh3QGm2zDohvJWOURwrD48zPVHDSGrkNCn4g-ayJi7gpYAhc4HUNyUjj7YCns0HnUKJXl3t1FmUCNjWFLg9MVeppijTki3vESZfVJGSPtBexMqug3nlXkA8pEcQnjxDbGFn7MyIc4cNnjbAQaIuCBRWKQSdT1keLD_O-_Tak4NFPhKRAP3nnFt2yJtEdJ82Wd4l2ac_vP0C6U-IZXCGQ6GJMdvLGCYug"}
)

# async def main():
#     url="http://127.0.0.1:8000/mcp"
#     async with streamablehttp_client(url) as (read,write,get_session_id):
#         async with ClientSession(read,write) as session:
#             result = await session.call_tool("add",{"a":2,"b":3})
#             print("result: ",result)

client=Client(transport)
async def main():
    async with client:
        tools=await client.list_tool()
        print(f"Available tools: {tools}")

asyncio.run(main()) 