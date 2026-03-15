import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.get_listings import get_internship_listings
from tools.compare_profiles import compare_profiles
from tools.get_best_matches import get_best_matches

listings = get_internship_listings("AI ML internship India")
results = compare_profiles(listings)
best = get_best_matches(results, 10)

print("TOP 3 MATCHES:")
print("=" * 40)
for job in best:
    print(f"{job['similarity_score']} — {job['job_title']}")
    print(f"Company: {job['employer_name']}")
    print(f"Apply: {job['apply_link']}")
    print("-" * 40)