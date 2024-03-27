# https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xe7270a41005252b6&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug2=0&rsv_btype=i&inputT=1166&rsv_sug4=2177

import requests

url = 'https://www.baidu.com/s'
kw = {'wd':'python'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
response = requests.get(url, params=kw, headers=headers)
print(response.url)
# print(response.content.decode('utf8')) # 长度2381
