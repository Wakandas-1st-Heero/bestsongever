from lib2to3.pgen2.pgen import generate_grammar
from operator import length_hint
from unicodedata import name
from main import access_token
import requests
import json
import xlsxwriter
import csv
import os
import pprint



headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '5sNESr6pQfIhL3krM8CtZn'
artist_id = '3nFkdlSjzX9mRTtwJOzDYB'

# actual GET request with proper header as of now you need to make one for each stat
t = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = requests.get(BASE_URL + 'audio-analysis/' + track_id, headers=headers)
h = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
s = requests.get(BASE_URL + 'artists/'+ artist_id, headers=headers)
v = requests.get(BASE_URL + 'recommendations/'+ track_id, headers=headers)


t_content = json.loads(t.content)
h_content = json.loads(h.content)
r_content = json.loads(r.content)
s_content = json.loads(s.content)
v_content = json.loads(v.)

print(v_content)
#print(s_content.get('genres'))