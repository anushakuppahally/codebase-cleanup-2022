import json
import requests

def fetch_data(url):
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response