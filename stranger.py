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

# artist = sp.artist(urn)
# print(artist)

#you need a print for each variable 
# r = r.json()
print(r)
# t = t.json()
# print(t)
# h = h.json()
# print(h)

#print(json.dumps(h.json(), indent=2))
# We make a request up above
# We grab the json from the response
#track_info = h.json()
#artist name 
#artist_info = h.json()
 
# We can now grab data from the json object (which is just a python Dictionairy)
# print(track_info['name'])
# print()

#song = track_info['name']

#time to dump data into excel these are the steps fopr xlsx
#worksheet = xlsxwriter.Workbook('hello.xlsx')

# workbook = xlsxwriter.Workbook('test.xsls')
# worksheet = workbook.add_worksheet('testsheet')



# with open("song_data.xlsx", "w") as xlsx_file:
#     xlsx_writer = xlsx.writer(xlsx_file)
#     xlsx_writer.writerow(["Song", "Artist"])
#     xlsx_writer.writerow([track_info['name']])


