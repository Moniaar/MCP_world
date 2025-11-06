from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
