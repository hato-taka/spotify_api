import requests
import base64

def get_spotify_access_token(client_id, client_secret):
    # Base64エンコードされた認証文字列を作成
    auth_string = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        'Authorization': f'Basic {auth_string}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {'grant_type': 'client_credentials'}

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Error getting access token: {response.status_code} - {response.text}")

# 使用例
client_id = 'あなたのClient ID'
client_secret = 'あなたのClient Secret'

try:
    access_token = get_spotify_access_token(client_id, client_secret)
    print(f"アクセストークン: {access_token}")
except Exception as e:
    print(str(e))