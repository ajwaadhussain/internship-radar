from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("firstServer")

@mcp.tool()
def get_user_profile():
    """Reads the user profile from profile.json and returns skills, domain, projects and experience."""
    data = json.load(open("profile.json"))
    return data