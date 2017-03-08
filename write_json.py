"""
    Downloads Seattle Permit database and save it
    to a json file stored in the media folder
"""

import requests
import json


# payload = {'action_type': 'CURB CUT'}

payload = {'permit_type': 'Construction'}
url = 'https://data.seattle.gov/resource/i5jq-ms7b.json'
data = requests.get(url, params=payload)
# data.json()

# Writing JSON data
with open('media/construction.json', 'w') as f:
    json.dump(data.json(), f)
