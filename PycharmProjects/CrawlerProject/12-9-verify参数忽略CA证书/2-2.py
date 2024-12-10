import requests
import json
class Tran(object):

    def __init__(self,word):
        self.url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_new_fanyi&sign=9X%2BHAviAKqteMMuVvr%2B0X9RriqVIAJSQ%2BxmfU0q7dIE%3D'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        self.data = {
          "f": "auto",
          "t": "auto",
          "q": word
        }

    def get_data(self):
        response = requests.post(self.url,data=self.data,headers  = self.headers)
        return response.content

    def run(self):
        '''爬虫逻辑'''
        '''
        url
        headers
        data
        response
        analysis
        '''
        response = self.get_data()
        print(response)

if __name__ == '__main__':
    obj = Tran('手机')
    obj.run()