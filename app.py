from flask import Flask, render_template, request

app = Flask(__name__)
HOST = "127.0.0.1"
# HOST = "5.104.108.237"
PORT = "14983"
PASSWORD = "238938"
ENCRIPTION = "AES-256-GCM"


class Settings:
    host = "5.104.108.237"
    port = "14983"
    password = "238938"
    encription = "AES-256-GCM"


class Links:
    android_client = (
        "https://play.google.com/store/apps/details?id=com.github.shadowsocks"
    )
    windows_client = "https://github.com/shadowsocks/shadowsocks-windows/releases/download/4.4.1.0/Shadowsocks-4.4.1.0.zip"
    ios_client = (
        "https://apps.apple.com/us/app/sockswitch-shadowsocks-client/id1453207024"
    )
    rutor = 'http://rutor.info/'
    rutracker = 'https://rutracker.org/forum/index.php'
    flibusta = 'https://flibusta.is/'
    instagram = 'https://www.instagram.com/'


@app.route("/")
def index():
    ip_addr = request.remote_addr
    check = ip_addr == Settings.host
    return render_template(
        "index.html",
        logo_img="static/logo.jpg",
        qr_img="static/qr.jpg",
        settings=Settings,
        links=Links,
        ip_addr=ip_addr,
        check=check
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=80)
