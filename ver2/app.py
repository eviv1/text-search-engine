from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"]

        # please insert the file location of the text here
        folder = r"C:\Users\IT\Downloads\JC FIles\JC FIles"
        context_chars = 100

        pattern = re.compile(re.escape(query), re.IGNORECASE)

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".txt"):
                    full_path = os.path.join(root, file)
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        filename = os.path.basename(f.name)

                        # match: filename
                        if pattern.search(filename):
                            results.append(f"<b><u>{filename}</u></b><br><small>{full_path}</small>")

                        # match: file content
                        for match in pattern.finditer(content):
                            start = max(0, match.start() - context_chars)
                            end = min(len(content), match.end() + context_chars)
                            snippet = content[start:end].replace('\n', ' ').strip()
                            results.append(f"<a href='{full_path}'>{filename}</a><br><small>{full_path}</small><br><br>...{snippet}...")

    return render_template("index ver 1.2.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

    # hyperlink: open text file on browser 
    # remove duplicate entries
    # do a table of contents, add pagination so that all text files would not load at once
    # automatic search filtering without pressing enter (search on the upper, then all txt files are on a table kahit 1 column lang)