from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("firstServer")

@mcp.tool()
def get_user_profile():
    """Reads the user profile from profile.json and returns skills, domain, projects and experience."""
    current_dir = os.path.dirname(__file__)
    profile_path = os.path.join(current_dir, "..", "profile.json")
    with open(profile_path) as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    mcp.run()