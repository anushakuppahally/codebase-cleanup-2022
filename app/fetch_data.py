import json
import requests

def fetch_data(url):
    response = requests.get(url)
    return json.loads(response.text)