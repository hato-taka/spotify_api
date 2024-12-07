import requests
import base64

from dotenv import load_dotenv
import os

# .env ファイルを読み込む
load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

auth_string = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_string}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {'grant_type': 'client_credentials'}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
access_token = response.json()['access_token']

# ユーザープロフィールの取得:

user_id = os.getenv('user_id')
url = f"https://api.spotify.com/v1/users/{user_id}"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)
user_profile = response.json()

print(f"ユーザー名: {user_profile['display_name']}")
print(f"フォロワー数: {user_profile['followers']['total']}")

# ユーザーのプレイリスト取得:

url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)
playlists = response.json()["items"]

for playlist in playlists:
    print(f"プレイリスト名: {playlist['name']}")