import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_key)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "AIとはなんですか？"}],
    stream=True,
    # トークン数を制限
    max_tokens=50,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
