import requests
import json

r = requests.get("https://www.soccer24.com/")

with open('comic.json', 'wb') as f:
	f.write(r.content)