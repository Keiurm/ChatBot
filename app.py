import openai
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)


client = OpenAI()

# 送信メッセージを保存するリスト
message_list = []

# 生成されたメッセージを保存するリスト
response_list = []


# 返信を生成
def generate_response(message, model):
    if len(message_list) == 1:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}],
        )
        response_list.append(completion.choices[0].message.content)
        return completion.choices[0].message.content
    else:
        messages = []
        for user_msg, assistant_msg in zip(message_list, response_list):
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
        messages.append({"role": "user", "content": message})

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        response_list.append(completion.choices[0].message.content)
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
    message_list.append(data["message"])
    return jsonify(generate_response(data["message"], data["model"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
