import os
import re

query = input("Enter search term: ")

folder = r"C:\Users\IT\Downloads\JC FIles\JC FIles"

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if re.search(query, content, re.IGNORECASE):
                    print(f"Match found in: {full_path}")
