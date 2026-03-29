import asyncio

import mcp
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client


params = StdioServerParameters(
    command="uv",
    args=["run", "date_mcp/date_server.py"],
    env=None,
)


async def list_date_tools():
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            tools_result = await session.list_tools()
            return tools_result.tools


async def call_date_tool():
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool("get_today_date", {})
            return result


async def main():
    tools = await list_date_tools()
    print("Available tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

    result = await call_date_tool()
    print("\nTool result:")
    print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
