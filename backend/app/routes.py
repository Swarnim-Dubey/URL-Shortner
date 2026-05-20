# from flask import Blueprint, request, jsonify, redirect
# import random
# import string

# routes = Blueprint('routes', __name__)

# url_db = {}

# def generate_short_code(length=6):
#     char = string.ascii_letters + string.digits
#     return ''.join(random.choice(char) for _ in range(length))

# @routes.route("/shorten", methods=["POST"])
# def shorten_url():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "no json file is recieved"}), 400
    
#     long_url = data.get("url")
#     custom_code = data.get("custom_code")
#     if not long_url:
#         return jsonify({"error": "URL is required"}), 400
    
#     if custom_code:
#         short_code = custom_code
#     else:
#         short_code = generate_short_code()

#     # save url
#     url_db[short_code] = long_url
#     short_url = f"http://127.0.0.1:5000/{short_code}"

#     return jsonify({"short_url": short_url})

# @routes.route("/<short_code>")
# def redirect_url(short_code):
#     long_url = url_db.get(short_code)
#     if long_url:
#         return redirect(long_url)
#     return "URL not found", 404

from flask import Blueprint, request, jsonify, redirect, send_from_directory
import random
import string
import os

routes = Blueprint("routes", __name__)

# temporary storage
url_database = {}

# frontend path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# =========================
# HOME PAGE
# =========================
@routes.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# =========================
# CSS + JS FILES
# =========================
@routes.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(
        os.path.join(FRONTEND_DIR, "assets"),
        filename
    )


# =========================
# SHORTEN URL
# =========================
@routes.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    long_url = data.get("url")
    custom_code = data.get("custom_code")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    if custom_code:
        short_code = custom_code
    else:
        short_code = generate_short_code()

    url_database[short_code] = long_url

    short_url = f"http://127.0.0.1:5000/{short_code}"

    return jsonify({
        "short_url": short_url
    })


# =========================
# REDIRECT
# =========================
@routes.route("/<short_code>")
def redirect_url(short_code):

    long_url = url_database.get(short_code)

    if long_url:
        return redirect(long_url)

    return "URL not found", 404