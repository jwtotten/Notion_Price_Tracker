import requests
import json
import time
import os
from dotenv import load_dotenv

# load in the .env file
load_dotenv()

# load in the NOTION_SECRET from the .env file
NOTION_TOKEN = os.getenv('NOTION_SECRET', '')

def get_cool_fact():
    r = requests.get('https://asli-fun-fact-api.herokuapp.com/')

    # Request failed, don't try to parse and just return None
    if not r.ok:
        return None

    # Parse JSON
    json_data = r.json()

    return json_data['data']

print(get_cool_fact())
