import spotipy
from venv import YOUR_APP_CLIENT_ID
from venv import YOUR_APP_CLIENT_SECRET
from spotipy.oauth2 import SpotifyClientCredentials
import requests

#sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=YOUR_APP_CLIENT_ID,
#                                                           client_secret=YOUR_APP_CLIENT_SECRET))
CLIENT_ID=YOUR_APP_CLIENT_ID,
CLIENT_SECRET=YOUR_APP_CLIENT_SECRET
grant_type = 'client_credentials'

# CLIENT_ID = 'yourid'
# CLIENT_SECRET = 'yoursecret'

url = 'https://accounts.spotify.com/api/token'

response = requests.post(url, {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
})

data = response.json()
access_token = data['access_token']

print(access_token)

