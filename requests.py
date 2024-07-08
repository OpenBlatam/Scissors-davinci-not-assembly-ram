#https://www.twitch.tv/rw_grim
import requests

response = requests.get('https://api.github.com/users/github')

print(response.json())
