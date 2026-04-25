import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

async def main():
    server = StdioServerParameters(
        command="python",
        args=["main.py"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as client:
            await client.initialize()

            tools = await client.list_tools()

            result = await client.call_tool("add", {"a": 5, "b": 3})
            print("🤖 Add result:", result.structuredContent["result"])

            result = await client.call_tool("get_weather", {"city": "Mumbai"})
            print("🤖 Weather:", result.structuredContent["result"])

asyncio.run(main())