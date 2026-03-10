import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.get_listings import get_internship_listings

results = get_internship_listings("AI ML internship India")

for job in results:
    print(job["job_title"], "-", job["employer_name"])