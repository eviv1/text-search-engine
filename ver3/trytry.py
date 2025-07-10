from flask import Flask, render_template, request
import os
import re
from urllib.parse import quote

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    folder = r"C:\Users\IT\Downloads\JC FIles\JC FIles"
    context_chars = 100
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    filename = os.path.basename(f.name)
                    snippet = content.replace('\n', ' ').strip()
                    filename_encoded = quote(filename)
                    clean_content = content.replace('\n', ' ').replace('\r', ' ')  # Optional: strip \r too
                    results.append(f'''
                    <tr>
                        <td><b><u>{filename}</u></b></td>
                        <td>
                            <button onclick="toggleContent(this)">Show</button>
                        </td>
                        <td>
                            <div class="content-snippet" style="display:none;">{clean_content}</div>
                        </td>
                    </tr>
                    ''')
    return render_template("experimentv1.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)