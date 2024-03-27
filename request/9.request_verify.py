import requests

url='http://www.baidu.com'

response = requests.get(url, verify=False)

# SSLerror:安全套件失败
print(response.content)