from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
import chromadb
import json
import os 

model = SentenceTransformer("all-MiniLM-L6-v2")
mcp = FastMCP("retrieve_listings")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("internship_listings")

@mcp.tool()
def retrieve_listings(n_results: int) -> list:
    """Retrieve the most relevant internship listings from ChromaDB based on the user profile."""
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
    profile_embedding = model.encode([profile_text])[0].tolist()
    results = collection.query(
        query_embeddings=[profile_embedding],
        n_results=n_results,
        include=["documents", "distances", "metadatas"]
    )

    cleaned = []
    for i in range(len(results['ids'][0])):
        cleaned.append({
            "job_title": results['metadatas'][0][i]['job_title'],
            "employer_name": results['metadatas'][0][i]['employer_name'],
            "apply_link": results['metadatas'][0][i]['apply_link'],
            "distance": results['distances'][0][i]
        })
    return cleaned

if __name__ == '__main__':
    mcp.run()