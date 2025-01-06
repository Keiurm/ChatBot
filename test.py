import os
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."},
    ],
)

print(completion.choices[0].message)
