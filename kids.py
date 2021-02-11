
from pathlib import Path
import random

Favourite_Kids = ["Ruby", "Nazrein", "Jason"]
Close_to_my_Heart = random.choice(Favourite_Kids)
print(Close_to_my_Heart)


path = Path("ecomerce")
print(path.rmdir())


path = Path()
for file in path.glob("*.py"):
    print(file)
