import mysql
import mysql.connector
from unicodedata import name
from main import access_token
import requests
import json
import xlsxwriter
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="song_metrics"
)


#--------------------------------------------------------------

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


#you need a print for each variable 
# r = r.json()
# print(r)
# t = t.json()
# print(t)
#h = h.json()
#print(h)


# We make a request up above
# We grab the json from the response
track_info = h.json()

#variable for artist name 
artist_info = h.json()
 
# We can now grab data from the json object (which is just a python Dictionairy)
print(track_info['name'])


#used to print the artist name, we can use this to extract certain info
result = artist_info['artists'][0]['name']
print(result)

mycursor = mydb.cursor() 
 

sql = "INSERT INTO spotify_list (artist_name, song, temp) VALUES (%s, %s, %f)" 
val = ("Some artist", "Highway 21", "0.12")
 
mycursor.execute(sql, val)
 
mydb.commit()
 
print(mycursor.rowcount, "record inserted.")