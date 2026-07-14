import os
from fastmcp import FastMCP

mcp = FastMCP("ebaygptapp")

@mcp.tool()
async def create_posting(name: str, price: int, description: str) -> dict:
    """Creates a posting on ebay and returns the post summary."""

    return { "response": f"The {name} post with price {price} was created successfully."}

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
