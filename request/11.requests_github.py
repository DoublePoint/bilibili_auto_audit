import re

import requests

url_login = 'https://github.com/login'

session = requests.session()
session.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
res_1 = session.get(url_login).content.decode()
token = re.findall('name="authenticity_token" value="(.*?)" />',res_1)
timestamp = re.findall('name="timestamp" value="(.*?)" />',res_1)
timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" />',res_1)

print(token)
print(timestamp)
print(timestamp_secret)
data = {'commit': 'Sign in',
    'authenticity_token': token,
    'login': '997820126@qq.com',
    'password': '203105800liulei',
    'webauthn-conditional': 'undefined',
    'javascript-support': 'true',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'unsupported',
    'return_to': 'https://github.com/login',
    'timestamp': timestamp,
    'timestamp_secret': timestamp_secret
}
print("Start requests url2.")
url2 = 'https://github.com/session'
res_2 = session.post(url=url2,data=data)
print("End requests url2.")
print("Start requests url3.")
url3 = 'https://github.com/'
res_3 = session.get(url3)
print("End requests url3.")
with open('github_login.html', 'wb') as f:
    f.write(res_3.content)

url2 = 'https://github.com/session'
