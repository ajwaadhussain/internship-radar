from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://jsearch.p.rapidapi.com/search"

mcp = FastMCP("get_listings")

@mcp.tool()
def get_internship_listings(search_query: str) -> list:
    """Search for internship listings matching a query and return job title, description, employment type, highlights, posted date and apply link for each listing."""
    querystring = {
        "query": search_query,
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "x-rapidapi-key": os.getenv("JSEARCH_API_KEY"),
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    listings = []

    for i in data["data"]:
        listings.append({
            "job_title": i['job_title'],
            "job_description": i['job_description'],
            "employment_type": i['job_employment_type'],
            "posted_date": i['job_posted_at'],
            "apply_link": i['job_apply_link'],
            "job_highlights": i.get('job_highlights', {}),
            "employer_name": i['employer_name']
        })
    return listings

if __name__ == "__main__":
    mcp.run()