# Gemini API 試し
import google.generativeai as genai

api_key = ""
genai.configure(api_key=api_key)

# 使用するモデルを選択
model = genai.GenerativeModel('gemini-2.5-flash')
# AIに生成させたい文章（プロンプト）
prompt = "赤点をとらない方法を教えて"
# テキストを生成
response = model.generate_content(prompt)
# 結果を表示
print(response.text)


# OpenAI API 試し
from openai import OpenAI

# OpenAI APIキーの設定
api_key = ""
client = OpenAI(api_key=api_key)

# テキスト生成をリクエスト
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "留年しない方法を教えて"}
  ]
)
# 結果を表示
print(response.choices[0].message.content)


# Claude API 試し
!pip install anthropic

from anthropic import Anthropic
api_key = ""
client = Anthropic(api_key=api_key)
# テキスト生成をリクエスト
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "愛とは"}
    ]
)

# 結果を表示
print(response.content[0].text)
