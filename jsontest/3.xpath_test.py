import requests
from lxml import etree
url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

session = requests.session()
session.headers = headers
response = session.get(url)
html = etree.HTML(response.content)
print(html.xpath("//h2//*/text()"))
# with open("testxpath.html","wb") as f:
#     f.write(response.content)

