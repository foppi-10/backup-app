from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

CLOUD_NAME = "dbiqygsjx"     # on remplira plus tard
API_KEY    = "838654343811734"
UPLOAD_URL = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/auto/upload"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "Pas de fichier"}), 400
    files = {"file": file.read()}
    data = {"upload_preset": "backup_preset", "api_key": API_KEY}
    r = requests.post(UPLOAD_URL, files=files, data=data)
    return r.json() if r.ok else (r.text, r.status_code)

if __name__ == "__main__":
    app.run(debug=True)

