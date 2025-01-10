from flask import Flask, render_template, request, jsonify
from redis import Redis
import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数を読み込む
load_dotenv()

openai_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_key)
app = Flask(__name__)


def generate_response():
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "こんにちは"}],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/t1")
def t1():
    return render_template("t1.html")


@app.route("/response", methods=["POST"])
def response():
    data = request.json
    generate_response()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
