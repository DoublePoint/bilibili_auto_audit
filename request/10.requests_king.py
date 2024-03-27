import jsontest
import sys

import requests

class King(object):
    def __init__(self,word):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        self.url = 'http://www.baidu.com'
        self.data = {
            'a1':'a1',
            'a2':'a2',
            'a3':word
        }

    def get_data(self):
        response = requests.post(url=self.url, headers=self.headers, data = self.data)
        return response.content

    def parse_data(self,data):
        # 将json字符串转成python字典
        dict_data = jsontest.loads(data)
        print(dict_data['content']['data'])

    def run(self):
        return self.getData()

if __name__ == '__main__':
    # word = input("请输入要翻译的单词或句子：")
    word = sys.argv
    # king = King()
    # print(king.run())
    print(word)