import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
from starlette.requests import Request
from starlette.responses import JSONResponse

verifier = StaticTokenVerifier(
    tokens={
        os.environ["API_TOKEN"]: {
            "client_id": "chatgpt",
            "scopes": ["api:access"]
        },
    },
    required_scopes=["api:access"]
)

mcp = FastMCP("ebaygptapp", auth=verifier)

# This one is unauthenticated healthcheck endpoint for the loadbalancer
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})

@mcp.tool()
async def word_count(text: str) -> dict:
    """Return basic counts for a block of text."""
    words = text.split()
    lines = text.splitlines()

    return {
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "words": len(words),
        "lines": len(lines),
    }

# run on a VM with "nohup uv run main.py > log.tmp 2>&1 &"
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
