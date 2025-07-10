import re
import os

for root, dirs, files in os.walk(r"C:\Users\IT\Documents\Codes"):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            print(full_path)



