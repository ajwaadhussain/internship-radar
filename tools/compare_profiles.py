from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
mcp = FastMCP("compare_profiles")

@mcp.tool()
def compare_profiles(listings: list) ->list:
    """Compare job listings with user profile and return the job listings with a similarity score."""
    current_dir = os.path.dirname(__file__)
    profile_path = os.path.join(current_dir, "..", "profile.json")
    with open(profile_path) as f:
        data = json.load(f)
    skills_list = []
    for category in data["skills"].values():
        skills_list.extend(category)
    skills_text = ", ".join(skills_list)
    projects_text = " ".join([p["name"] + " " + p["description"] for p in data["projects"]])
    profile_text = f"{data['degree']} {data['specialization']} {' '.join(data['seeking_roles'])} {skills_text} {projects_text}"
    profile_embedding = model.encode([profile_text])
    results = []
    for i in listings:
        job_text = f"{i['job_title']} {i['job_description']}{str(i['job_highlights'])}"
        job_embedding = model.encode([job_text])
        score = cosine_similarity(profile_embedding, job_embedding)[0][0]
        i['similarity_score'] = round(float(score),4)
        results.append(i)
    return results

if __name__ == "__main__":
    mcp.run()