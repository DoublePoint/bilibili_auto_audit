import requests

url = 'http://www.baidu.com'

response = requests.get(url)
# 打印编码格式
# print(response.encoding)
# 修改编码格式，修改之后就能正确的显示中文汉字
# response.encoding='utf8'
# 打印响应的内容
# print(response.text)
# print(response.encoding)

# 或者 response.content是村粗的bytes类型的响应源码，
# print(response.content)
# print(response.content.decode()) # 默认utf-8
# print(response.content.decode("GBK")) #gbk gb2312 ascii iso-8859-1

# 相应状态吗
print(response.status_code)
# 响应对应的请求头
print(response.requests.headers)
# 响应的响应头
print(response.headers)
# 响应的Cookie,与response.headers中的Set-Cookie
print(response.cookies)