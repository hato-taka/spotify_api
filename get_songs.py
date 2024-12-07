import requests
from dotenv import load_dotenv
import os

# .env ファイルを読み込む
load_dotenv()

token = os.getenv('token')
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.spotify.com/v1/me/player/recently-played', headers=headers)
recently_played = response.json()

for item in recently_played['items']:
    track = item['track']
    print(f"曲名: {track['name']}")
    print(f"アーティスト: {track['artists'][0]['name']}")
    print(f"再生日時: {item['played_at']}")
    print("---")