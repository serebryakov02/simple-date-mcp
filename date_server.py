# Simple MCP notes:
# - Server: the program that exposes tools. In this file, the server offers a date tool.
# - Client: the program that connects to the server and asks for its tools or calls them.
# - Host: the app that uses the client. For example, a notebook, a script, or an AI app can be the host.
# - Tool: a function the server makes available to the outside world.
# - Transport: how messages move between client and server. Here we use "stdio",
#   which means they talk through standard input and standard output.
# - Common pattern: keep your real logic in plain Python functions, then expose only the
#   functions you want as MCP tools.

from datetime import date

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("date_server")


@mcp.tool()
async def get_today_date() -> str:
    """Return today's date in YYYY-MM-DD format."""
    return date.today().isoformat()


if __name__ == "__main__":
    mcp.run(transport="stdio")
