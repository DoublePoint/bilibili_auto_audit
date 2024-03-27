import requests


url = 'http://www.baidu.com'
proxies = {
    'http':'127.0.0.1:7897',
    'https':'127.0.0.1:7897'
}

response = requests.get(url, proxies=proxies)
response.encoding='utf8'
print(response.text)