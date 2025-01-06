from flask import Flask, render_template, request, jsonify
from redis import Redis
import os
from dotenv import load_dotenv
from openai import OpenAI
from io import BytesIO
import numpy as np

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    redis.incr("hits")
    return render_template("chat.html", conversation="Hello")


def get_openai_key():
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")


@app.route("/chat", methods=["POST"])
def chat():
    #APIKeyの取得
    get_openai_key()





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
