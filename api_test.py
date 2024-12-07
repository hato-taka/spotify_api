import requests
import base64
import json

from dotenv import load_dotenv
import os

# .env ファイルを読み込む
load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Base64エンコードされた認証文字列を作成
auth_string = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_string}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {'grant_type': 'client_credentials'}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
token = json.loads(response.content)['access_token']

# APIの使用例

headers = {'Authorization': f'Bearer {token}'}
query = 'q=ドラえもん&type=track'
response = requests.get(f'https://api.spotify.com/v1/search?{query}', headers=headers)
results = json.loads(response.content)

for track in results['tracks']['items']:
    print(f"{track['album']['name']} : {track['name']}")