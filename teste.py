from parse import findall
import requests
import json
import  numpy as np
import re


response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/2/lookupplayer.php?id=34145937")
json_response = response.json()
dictionary = json.dumps(json_response, sort_keys=True, indent=1)
#s = []
#for r in findall('"idPlayer": "{}", ', dictionary):
    #s.append(r[0])

#print(len(s))
#print(s)
print(dictionary)



