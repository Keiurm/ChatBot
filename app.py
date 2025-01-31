import openai
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)


# OpenAI APIのクライアントを作成
client = OpenAI()

# 送信メッセージを保存するリスト
message_list = []

# 生成されたメッセージを保存するリスト
response_list = []


# 返信を生成
def generate_response(message, model):
    # 最初のメッセージの場合
    if len(message_list) == 1:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}],
        )
        response_list.append(completion.choices[0].message.content)
        return completion.choices[0].message.content
    # 2回目以降のメッセージの場合
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
        # モデル名を公式の表現に変更
        if model == "gpt-4o-mini":
            model = "GPT-4o-mini"
        elif model == "gpt-4o":
            model = "GPT-4o"
        elif model == "o1-mini":
            model = "o1 mini"
        else:
            model = "o1-preview"
        return [completion.choices[0].message.content, model]


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/response", methods=["POST"])
def response():
    data = request.json
    # メッセージを保存
    message_list.append(data["message"])
    # 返信を生成
    return jsonify(generate_response(data["message"], data["model"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
