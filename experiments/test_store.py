import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.get_listings import get_internship_listings
from tools.store_listings import store_listings

listings = get_internship_listings("AI ML internship India")
result = store_listings(listings)
print(result)