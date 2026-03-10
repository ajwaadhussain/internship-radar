import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query": "AI ML internship India",
    "page": "1",
    "num_pages": "1"
}

headers = {
    "x-rapidapi-key": os.getenv("JSEARCH_API_KEY"),
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

first_job = data["data"][0]
print(first_job.keys())

print(first_job['job_highlights'])
print("---")
print(first_job['job_description'][:300])