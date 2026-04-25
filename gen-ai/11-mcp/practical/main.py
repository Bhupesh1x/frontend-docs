import requests
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Simple MCP Server")

# Tools
@mcp.tool()
def add(a: int, b: int) -> int:
  """Add two numbers"""
  print("Tool called: add", a, b)
  return a + b

@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    print("Tool called: get_weather", city)

    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return f"The weather in {city} is {response.text.strip()}."
        else:
            return f"Failed to fetch weather for {city}."

    except Exception as e:
        return f"Error fetching weather: {str(e)}"

mcp.run()