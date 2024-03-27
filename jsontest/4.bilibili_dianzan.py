import requests

url1 = 'https://search.bilibili.com/all?keyword=%E4%BA%92%E5%85%B3%E4%BA%92%E8%B5%9E'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

session = requests.session()
session.headers = headers
response = session.get(url1)
with open("bizandianzan.html","wb") as f:
    f.write(response.content)