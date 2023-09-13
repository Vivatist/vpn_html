from flask import Flask, render_template, request
from links import Links

app = Flask(__name__)
HOST = "127.0.0.1"
# HOST = "5.104.108.237"
PORT = "14983"
PASSWORD = "238938"
ENCRIPTION = "AES-256-GCM"


class Settings:
    host = "127.0.0.1"
    port = "14983"
    password = "238938"
    encription = "AES-256-GCM"


@app.route("/")
def index():
    ip_addr = request.remote_addr
    check = ip_addr == Settings.host
    return render_template(
        "index.html",
        logo_img="static/logo.png",
        qr_img="static/qr_img.png",
        settings=Settings,
        links=Links,
        ip_addr=ip_addr,
        check=check,
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=80)
