import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.retrieve_listings import retrieve_listings

results = retrieve_listings(3)

for job in results:
    print(f"Distance : {job['distance']:.4f}")
    print(f"Title    : {job['job_title']}")
    print(f"Company  : {job['employer_name']}")
    print(f"Apply    : {job['apply_link']}")
    print("-" * 60)