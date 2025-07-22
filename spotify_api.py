import requests
import base64

def get_token(client_id, client_secret):
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    data = {"grant_type": "client_credentials"}
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return r.json()["access_token"]

def get_genres(artist_name, token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1", headers=headers)
    try:
        return r.json()["artists"]["items"][0]["genres"]
    except:
        return []
