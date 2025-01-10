import openai
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)


client = OpenAI()


# 返信を生成
def generate_response(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content": message}],
    )
    return completion.choices[0].message.content


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/t1")
def t1():
    return render_template("t1.html")


@app.route("/response", methods=["POST"])
def response():
    data = request.json
    return jsonify(generate_response(data["message"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
