from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Route gốc để tránh lỗi 404 khi truy cập trang chủ
@app.route("/", methods=["GET"])
def home():
    return "✅ Plugin 2styLife đã hoạt động!"

# Trả về file ai-plugin.json cho ChatGPT
@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def serve_ai_plugin():
    return send_from_directory(".well-known", "ai-plugin.json", mimetype="application/json")

# Trả về file openapi.yaml
@app.route("/openapi.yaml", methods=["GET"])
def serve_openapi():
    return send_from_directory(".", "openapi.yaml", mimetype="text/yaml")

# API mẫu để ChatGPT gọi đến
@app.route("/get-socials", methods=["GET"])
def get_social_links():
    return jsonify({
        "website": "https://2stylife.com",
        "instagram": "https://www.instagram.com/lifestyle.thesecond/",
        "facebook": "https://www.facebook.com/LifeStyle.TheSecond"
    })

# Khởi động server (dùng biến môi trường PORT nếu có)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
