import requests

url = 'https://github.com/DoublePoint'

# 不带请求头
response = requests.get(url)
print(len(response.content)) # 长度2381

# 告诉服务器，我是浏览器
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
cookie_str = "_octo=GH1.1.934139043.1688095229; _device_id=20efc90c28fa06a4c9c856b9bddcf3d6; user_session=PsmnQXXMdFowpVxFKntmNRhLxCz9M7iglSilNglMbOpwSk5a; __Host-user_session_same_site=PsmnQXXMdFowpVxFKntmNRhLxCz9M7iglSilNglMbOpwSk5a; logged_in=yes; dotcom_user=DoublePoint; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light_colorblind%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_colorblind%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=gTtQaUdw1wvaycAoMpKLcsstJ8eLbs4BxmzOrPrNmWBqfDakXsDC%2FpuU%2FF%2ByPav1ImISwVszrBD4wvavMKbRH%2Bhw6WCplHmAXNrSyUhtc3vGbTPqjfMKHbJOpl4vMlmibR9%2FZBaIqDHz5b8TTUabQcdfacOkbxVQg64pNUsDOjEA8gmlEwHEW2Zr4f2VCJlA1%2FDxKFjcFiejlHmL2WycEXxD1aLebQDNbtOaq5MDxzJjvSGqeJYnNGEyCOrNxeJHHDbOSVWBDCM%2BkoOJgos3%2FjJ3mXvsWteXGCc90iQrDpPJvF%2F7fgzfK6MaLzQaVNAbOIQymYFNBIoJlNNmUv37PgBcwU35cHZmzbRmH2HKEgP9i2uR%2FZIACIhTDnG%2FlJZz9Q3Ybc2pOtMX0Gqu84pM6c4eNobpFH%2FzCmSQRAYP5CwaPqZHdDWHKm%2BrBRKmrAjO%2B5NtZAy96LYb%2FxoqlM1HEkm4YIgza%2FdRPhq9C2BFSKwQoieCq6tgETjXCelTs9yhBP9UgqSN3XRhLN3T1FgX6NN4WDsW7tXJEePtTTgbLxOdxF1UPccbQYQRB%2F3OvpKA6iPFGOJ1DNrIfoMFVQGqfMJghK1Y26k%2B8ll64HmpL%2Balx1MgKxKcohJ9Fcf5iW9e0WUz7jaWYIjnpLEXWSW%2FJKTrObUGGVA9qmjUvsYG%2BGeeGZsRZt6W8BlNJW6IpODjJoYG5o0rj%2BN2cGORnauizyMKKcwssAb1dt5C2pWXoWKGk4fMXu%2BjRq9ddvdfrwHG6u4DoDcALW94Z1fNrjvbP7wGWB8V6MYNHlxdTKL%2BXQiZlvwxWrbI4jg%2Fam91Vr%2FlyXcNlKUj%2B0xtzgoYc8uiNT21y0UYuMvVg0lc%2F%2BqVcw2gTQWC9271SJBD6JFruR245H9sGUOs7Bj9v0B6PrBpBXVnzXM%3D--0ELLXXxWcb0ALRxS--3hDbXS1H%2BINC8zbSJvjyeQ%3D%3D"
# 构建字典
cookie_list = cookie_str.split("; ")
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split("=")[0]]=cookie.split("=")[-1]

cookies = {cookie.split("=")[0]:cookie.split("=")[-1] for cookie in cookie_list}
print(cookies)
response = requests.get(url, headers=headers, cookies=cookies)
with open('github_with_cookie3.html', 'wb') as f:
    f.write(response.content)
