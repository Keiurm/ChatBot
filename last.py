from flask import Flask, render_template, request
from redis import Redis
import os
from dotenv import load_dotenv
from openai import OpenAI


app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    redis.incr("hits")
    return render_template("chat.html", conversation="Hello")


def get_openai_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
