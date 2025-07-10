import os
import re

query = input("Enter search term: ")
folder = r"C:\Users\IT\Downloads\JC FIles\JC FIles"
context_chars = 100  # characters before and after the match

pattern = re.compile(re.escape(query), re.IGNORECASE)  # Safe search pattern

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                filename = os.path.basename(f.name)

                # Search in filename
                if pattern.search(filename):
                    print(f"Match in filename: {full_path}\n")

                # Search in content
                for match in pattern.finditer(content):
                    start = max(0, match.start() - context_chars)
                    end = min(len(content), match.end() + context_chars)
                    snippet = content[start:end].replace('\n', ' ').strip()
                    print(f"Match in file: {full_path}")
                    print(f"...{snippet}...\n")
