from flask import Flask, render_template, request
from redis import Redis


app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/t1")
def t1():
    return render_template("t1.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
