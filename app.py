from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/.well-known/ai-plugin.json")
def serve_manifest():
    return send_from_directory(".well-known", "ai-plugin.json")

@app.route("/openapi.yaml")
def serve_openapi():
    return send_from_directory(".", "openapi.yaml")
    
@app.route("/products")
def products():
    return jsonify([
        {
            "name": "Túi Tote",
            "link": "https://2stylife.com/tote-bag/"
        },
        {
            "name": "Túi đeo chéo",
            "link": "https://2stylife.com/tui-deo-cheo-cac-loai/"
        },
        {
            "name": "Túi cầm tay",
            "link": "https://2stylife.com/clutch-pouch/"
        },
        {
            "name": "Ví da",
            "link": "https://2stylife.com/wallet/"
        }
    ])

@app.route("/instagram-posts")
def insta():
    return jsonify([
        {
            "caption": "New drop lên kệ hôm nay! ✨",
            "link": "https://www.instagram.com/lifestyle.thesecond/"
        }
    ])

@app.route("/facebook-posts")
def fb():
    return jsonify([
        {
            "title": "Bộ sưu tập túi da Ý mới đã về!",
            "link": "https://www.facebook.com/LifeStyle.TheSecond/"
        }
    ])

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
