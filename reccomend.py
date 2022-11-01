
from lib2to3.pgen2.pgen import generate_grammar
from operator import length_hint
from unicodedata import name
from unittest import result
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


#for all known ranges, best for using with genre and artist

limit = 1
seed_genres=""
seed_artists = "4NHQUGzhtTLFvgF5SZesLK,3RNrq3jvMZxD9ZyoOZbQOD,6XyY86QOPPrYVGvF9ch6wz,3nFkdlSjzX9mRTtwJOzDYB"
seed_tracks = ""
target_tempo = ".50"
target_danceability = ".050"
target_liveness = ".50"
target_popularity = ".50"
target_acousticness = ".50"
target_energy = ".50"
target_instrumentalness = ".50"
target_key = ".50"
target_speechiness = ".50"
target_valence = ".50"



endpoint_url = "https://api.spotify.com/v1/recommendations?"
query = f'{endpoint_url}limit={limit}&seed_genres={seed_genres}&seed_tracks={seed_tracks}&seed_artists={seed_artists}'
query += f'&target_tempo={target_tempo}'
query += f'&target_danceability={target_danceability}'
query += f'&target_liveness={target_liveness}'
query += f'&target_popularity={target_popularity}'
query += f'&target_acousticness={target_acousticness}'
query += f'&target_energy={target_energy}'
query += f'&target_instrumentalness={target_instrumentalness}'
query += f'&target_key={target_key}'
query += f'&target_speechiness={target_speechiness}'
query += f'&target_valence={target_valence}'


# print(query)
result = requests.get(query,headers=headers)

result_content = json.loads(result.content)
pprint.pprint(result_content, compact=True)







