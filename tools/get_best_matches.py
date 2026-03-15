from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("get_best_matches")

@mcp.tool()
def get_best_matches(results : list,top_n : int):
    """Sort the listings in Descending Order and return top 5 job listings."""
    sorted_result = sorted(results, key=lambda x: x["similarity_score"], reverse=True)
    return sorted_result[:top_n]
if __name__ == "__main__":
    mcp.run()

