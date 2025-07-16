# Gemini API 試し
import google.generativeai as genai

api_key = "AIzaSyBcLqmexB1vIvrJBwyjq1U0EtNLRAqHa-0"
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
api_key = "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"
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
api_key = "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"
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
