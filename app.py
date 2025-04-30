from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Kiểm tra trạng thái
@app.route("/")
def index():
    return "✅ Plugin 2styLife đã hoạt động!"

# Plugin manifest
@app.route("/.well-known/ai-plugin.json")
def serve_manifest():
    return send_from_directory(".well-known", "ai-plugin.json")

# OpenAPI schema
@app.route("/openapi.yaml")
def serve_openapi():
    return send_from_directory(".", "openapi.yaml")

# Danh sách sản phẩm
@app.route("/products", methods=["GET"])
def products():
    return jsonify([
        {"name": "Túi Tote", "link": "https://2stylife.com/tote-bag/"},
        {"name": "Túi đeo chéo", "link": "https://2stylife.com/tui-deo-cheo-cac-loai/"},
        {"name": "Túi cầm tay", "link": "https://2stylife.com/clutch-pouch/"},
        {"name": "Ví da", "link": "https://2stylife.com/wallet/"}
    ])

# Bài viết Instagram
@app.route("/instagram-posts", methods=["GET"])
def insta():
    return jsonify([
        {
            "caption": "New drop lên kệ hôm nay! ✨",
            "link": "https://www.instagram.com/lifestyle.thesecond/"
        }
    ])

# Bài viết Facebook
@app.route("/facebook-posts", methods=["GET"])
def fb():
    return jsonify([
        {
            "title": "Bộ sưu tập túi da mới đã về!",
            "link": "https://www.facebook.com/LifeStyle.TheSecond/"
        }
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
