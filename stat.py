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


t_content = json.loads(t.content)
h_content = json.loads(h.content)
r_content = json.loads(r.content)

#print(r_content)

# with open('data.json', 'w') as f:
#     json.dump(r_content, f)

#dict is the data types get is how the data is pulled from keys
# print(h_content.get('album').get('album_type'))
# print(h_content.get('album').get("bumbum_type", "You Failed Me Bro"))


#list store data to pull and can be pulled out of order or seperately
#(you get the data by pulling from the index)
#twitch_chat = ['JCWHITE', 'MachineGUn', 'Hero']
#print(twitch_chat[1])


#twitch_chat = ['JCWHITE', 'MachineGUn', 'Hero', {"count_of_message":"1337"}]
# print(twitch_chat[3].get('count_of_message'))

#you have 2 choices here loop it all to do less
#or print each one seen below
track_id_info = {
"artists_name" : h_content.get('artists')[0].get('name'),
"spotify_track_id" : h_content.get('artists')[0].get('id'),
"album_name" : h_content.get('album').get('name'),
"album_release_date" : h_content.get('album').get('release_date'),
"total_tracks" : h_content.get('album').get('total_tracks'),
'duration_min' : h_content.get('duration_ms')//1000/60,
'BPM' : t_content.get('tempo'),
'danceabilty' : t_content.get('danceabilty'),
'energy' : t_content.get('energy'),
'loudness' : t_content.get('loudness'),
'mode' : t_content.get('mode'),
'speechiness' : t_content.get('speechiness'),
'acousticness' : t_content.get('acousticness'),
'instrumentalness' : t_content.get('instrumentalness'),
'liveness' : t_content.get('liveness'),
'valence' : t_content.get('valence'),
'time_signature' : t_content.get('time_signature'),
'time_signature_confidence' : r_content.get('track').get('time_signature_confidence'),
'end_of_fade_in' : r_content.get('track').get('end_of_fade_in'),
'start_of_fade_out' : r_content.get('track').get('start_of_fade_out'),
'tempo_confidence' : r_content.get('track').get('tempo_confidence'),
'mode_confidence' : r_content.get('track').get('mode_confidence'),
'key_confidence' : r_content.get('track').get('key_confidence'),
#'bar' : r_content.get('bar').get('start'), insert
}
print(track_id_info)


#print(bopm)
#print(t_content)
## time_signature = estimated time signature for beats per measure
## mode = 1 is major 0 is minor
## Key Guide = The key the track is in. Integers map to pitches
## using standard Pitch Class notation.
## E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
##