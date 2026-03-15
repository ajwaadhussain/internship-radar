from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
mcp = FastMCP("store_listings")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("internship_listings")

@mcp.tool()
def store_listings(listings: list) -> str:
    """Embed job listings and store them in ChromaDB for later retrieval. Returns confirmation message."""
    new_count = 0
    for i in listings:
        existing = collection.get(ids=[i['job_id']])
        if existing['ids']:
            continue
        job_text = f"{i['job_title']} {i['job_description']}{str(i['job_highlights'])}"
        embedding = model.encode([job_text])[0].tolist()
        collection.add(
            ids=[i['job_id']],
            embeddings=[embedding],
            documents=[job_text],
            metadatas=[{
                "job_title": str(i['job_title'] or ""),
                "employer_name": str(i['employer_name'] or ""),
                "apply_link": str(i['apply_link'] or ""),
                "posted_date": str(i['posted_date'] or "")
            }]
        )
        new_count += 1

    return f"Stored {new_count} listings. {len(listings)- new_count} Already exists in ChromaDB"


if __name__ == "__main__":
    mcp.run()
