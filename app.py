from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)

# WooCommerce API credentials (bạn thay bằng key thật)
WC_API_URL = "https://2stylife.com/wp-json/wc/v3/products"
WC_CONSUMER_KEY = os.environ.get("WC_KEY", "ck_cc0c9188a7c611bc4518ee9a5e2c6b30f292da9c")
WC_CONSUMER_SECRET = os.environ.get("WC_SECRET", "cs_61a60637b7d492a04b220dab48bcc8503084ca58")

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

# Danh sách sản phẩm thực tế từ WooCommerce
@app.route("/products", methods=["GET"])
def products():
    try:
        response = requests.get(
            WC_API_URL,
            auth=HTTPBasicAuth(WC_CONSUMER_KEY, WC_CONSUMER_SECRET),
            params={"per_page": 10, "orderby": "date", "stock_status": "instock"}
        )
        response.raise_for_status()
        data = response.json()
        result = [
            {"name": p["name"], "link": p["permalink"]}
            for p in data
        ]
        return jsonify(result)
    except Exception as e:
        # Fallback dữ liệu nếu lỗi
        return jsonify([
            {"name": "Túi Tote", "link": "https://2stylife.com/totebag/?orderby=date"},
            {"name": "Túi Đeo Chéo", "link": "https://2stylife.com/deocheo/?orderby=date"},
            {"name": "Clutch Bag", "link": "https://2stylife.com/clutch/?orderby=date"},
            {"name": "Balo", "link": "https://2stylife.com/balo/?orderby=date"},
            {"name": "Túi Công Sở", "link": "https://2stylife.com/tuicongso2nd/?orderby=date"},
            {"name": "Túi Du Lịch", "link": "https://2stylife.com/2ndtravelbag/?orderby=date"},
            {"name": "Áo Các Loại", "link": "https://2stylife.com/2ndaocacloai/?orderby=date"},
            {"name": "Túi & Phụ Kiện Khác", "link": "https://2stylife.com/ortheritems/"},
            {"name": "Ví da", "link": "https://2stylife.com/wallet/?orderby=date/"}
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
