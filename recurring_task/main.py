import requests
import json
import time
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# load in the .env file
load_dotenv()

# load in the NOTION_SECRET from the .env file
NOTION_TOKEN = os.getenv('NOTION_SECRET', '')

def get_cool_fact():
    # address = 'https://asli-fun-fact-api.herokuapp.com/'
    address = 'https://www.amazon.co.uk/SanDisk-Extreme-Portable-1050MB-Dust-Resistant/dp/B0C59G4TLQ/ref=sr_1_6?crid=1FJ7NTVCBHA7A&dib=eyJ2IjoiMSJ9.Jr6xsq7WXhdoWjSm4fW3cPQ33QMvkjvdZlnKwe49WNe8vHB6A75lDCUAsDB41t5ki7QSQf-ZRWiaovuJh4IWF3bZwXvluIJ-CAc5uSAjcI2wTd26QE4Zmz-ygdAJ355jESIaCgj8RKsACT84aAJAcuFGvWRBNPur_uKWcoo81gzVdZM1vhv8KGwZm9LpATWHSbfOvq70xijS3ypkhO44oW1cQPBKh-kN7KRilUqXy-8.rKeYaInljpsICNCbawr4QmkTZncBiLX5yea3eGig2cU&dib_tag=se&keywords=ssd&qid=1733343349&s=videogames&sprefix=ss%2Cvideogames%2C158&sr=1-6&ufe=app_do%3Aamzn1.fos.f5096adf-5318-4e64-9ded-07ecefb9f39c&th=1'
    r = requests.get(address)
    r.raise_for_status()
    if r.status_code != 204:
        json_data = r.text

        html = BeautifulSoup(json_data, 'html.parser')
        return html.body.get_text().strip()
        
    # Request failed, don't try to parse and just return None
    if not r.ok:
        print('Failed to make request to selected site.')
        return None

print(get_cool_fact())
