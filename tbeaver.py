# import csv
# with open("song_data.csv", "w") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["Song", "Artist"])

from unicodedata import name
from main import access_token
import requests
import json
import xlsxwriter
import csv


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6xpDh0dXrkVp0Po1qrHUd8'

# actual GET request with proper header as of now you need to make one for each stat
t = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = requests.get(BASE_URL + 'audio-analysis/' + track_id, headers=headers)
h = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)

r = r.json()
print(r)
#t = t.json()
# print(t)
# h = h.json()
# print(h)