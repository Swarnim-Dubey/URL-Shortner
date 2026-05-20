from flask import (Flask,send_from_directory,request,jsonify,redirect)
from pathlib import Path
from backend.app.models import create_table
from backend.app.utils import generate_short_code
from backend.qr.qr import generate_qr_code
from backend.database.db import get_db_connection

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
ASSETS_DIR = FRONTEND_DIR / "assets"

QR_DIR = ASSETS_DIR / "qr"
print("BASE_DIR:", BASE_DIR)
print("FRONTEND_DIR:", FRONTEND_DIR)
print("ASSETS_DIR:", ASSETS_DIR)


app = Flask(__name__)
create_table()

@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )

@app.route("/assets/<path:path>")
def send_asset(path):

    return send_from_directory(
        ASSETS_DIR,
        path
    )

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({
            "error": "URL is required"
        }), 400

    custom_code = data.get("custom_code")

    if custom_code:
        short_code = custom_code
    else:
        short_code = generate_short_code()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO urls (
                original_url,
                short_code
            )
            VALUES (?, ?)
            """,
            (original_url, short_code)
        )
        conn.commit()

    except Exception:
        conn.close()
        return jsonify({
            "error": "Short code already exists"
        }), 400
    conn.close()

    short_url = f"http://localhost:5000/{short_code}"
    qr_filename = f"qr_{short_code}.png"
    qr_path = QR_DIR / qr_filename

    generate_qr_code(short_url)
    return jsonify({
        "short_url": short_url,
        # "qr_code": f"/assets/qr/{qr_filename}"
    })

@app.route("/<short_code>")
def redirect_to_url(short_code):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT original_url
        FROM urls
        WHERE short_code = ?
        """,
        (short_code,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(
            result["original_url"]
        )

    return jsonify({
        "error": "URL not found"
    }), 404

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)
