from parse import findall
import requests
import json
import  numpy as np
import re

from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.type_api import NULLTYPE

response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/2/searchplayers.php?p=Danny%20Welbeck")
json_response = response.json()
dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False, indent=1)
print(dictionary)




