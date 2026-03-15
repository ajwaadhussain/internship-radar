import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.get_listings import get_internship_listings
from tools.compare_profiles import compare_profiles

listings = get_internship_listings("AI ML internship India")
results = compare_profiles(listings)

for job in results:
    print(f"{job['similarity_score']} — {job['job_title']}")