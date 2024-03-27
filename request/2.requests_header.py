import requests

url = 'http://www.baidu.com'

# 不带请求头
response = requests.get(url)
print(len(response.content)) # 长度2381

# 告诉服务器，我是浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
print(len(response.content)) # 长度407428