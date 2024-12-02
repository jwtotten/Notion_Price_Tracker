import requests
import json
import time
import os
from dotenv import load_dotenv

# load in the .env file
load_dotenv()

# load in the NOTION_SECRET from the .env file
NOTION_TOKEN = os.getenv('NOTION_SECRET', '')
