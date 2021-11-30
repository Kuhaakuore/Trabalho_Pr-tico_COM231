from parse import findall
import requests
import json
import  numpy as np
import re

from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.type_api import NULLTYPE

list_dict = []
response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/2/searchloves.php?u=zag")
json_response = response.json()
dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False)
s = []
x = 0
for r in findall('"idPlayer": "{}", ', dictionary):
      id = str(r[0])
      actual_response = requests.get(
        "https://www.thesportsdb.com/api/v1/json/2/lookupplayer.php?id="+id)
      actual_json_response = actual_response.json()
      actual_dictionary = json.dumps(actual_json_response, sort_keys=True, ensure_ascii=False)
      list_dict.append(actual_dictionary)
      break


aux = []
for r in findall('"strSport": "{}", ', list_dict[0]):
        aux.append(r[0])
dados = np.asanyarray(aux)
print(dados)
exit()
my_list = set(s)
print(len(my_list))