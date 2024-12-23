import requests
import base64
from dotenv import load_dotenv
import os

# 認証情報
# .env ファイルを読み込む
load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
code = os.getenv('code')
redirect_uri = 'http://localhost:8888/callback'

# Base64エンコードされた認証文字列を作成
auth_string = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

# トークンを取得するためのリクエスト
headers = {
    'Authorization': f'Basic {auth_string}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect_uri
}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print(f"アクセストークン: {access_token}")
else:
    print("エラー:", response.status_code, response.text)