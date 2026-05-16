from flask import Flask, send_from_directory, request, jsonify, redirect
from backend.app.models import create_table
from backend.app.utils import generate_short_code
from backend.database.db import get_db_connection

app = Flask(__name__)
create_table()

@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")

@app.route("/assets/<path:path>")
def send_asset(path):
    return send_from_directory("../frontend/assets", path)

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data["url"]
    # if not original_url:
    #     return jsonify({"error": "URL is required"}), 400

    # short_code = generate_short_code()
    custom_code = data.get("custom_code")
    if custom_code:
        short_code = custom_code
    else:
        short_code = generate_short_code()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
                   (original_url, short_code))
    conn.commit()
    conn.close()

    return jsonify({"short_code": short_code}), 201

@app.route("/<short_code>" )
def redirect_to_url(short_code):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result["original_url"])
    return{
        "error": "URL not found"
    }, 404

if __name__ == "__main__":
    
    print("Starting Flask Server...")
    app.run(debug=True)