import requests

response = requests.get('https://api.github.com/users/github')

print(response.json())
