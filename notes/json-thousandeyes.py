import requests

url = 'https://api.thousandeyes.com/v6/tests.json'

r = requests.post(url,)

data = r.json()
print(data)