import requests
import json

with open('song.mp3', 'rb') as f:
    song = f.read()

files = {"file": song}

# json.loads

response = requests.post("http://0.0.0.0:8000/process_audio", files=files)
# response = requests.get("http://0.0.0.0:8000/process_audio")
print(response.text, response.status_code)