from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebaygptapp", host="0.0.0.0", port=8000)

@mcp.tool()
def word_count(text: str) -> dict:
    """Return basic counts for a block of text."""
    words = text.split()
    lines = text.splitlines()

    return {
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "words": len(words),
        "lines": len(lines),
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
