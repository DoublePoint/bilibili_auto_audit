import requests

url = 'http://www.twitter.com'

response = requests.get(url, timeout=3)

print(response)