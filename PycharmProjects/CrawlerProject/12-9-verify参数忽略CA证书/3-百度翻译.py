
import requests

class Tran(object):

    def __init__(self,word):
        self.url = "https://fanyi.baidu.com/sug"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        self.data = {
            "kw":word
        }

    def Getdata(self):
        response = requests.post(url=self.url, data=self.data,headers=self.headers)
        return response.content

    def Run(self):
        response = self.Getdata()
        print(response)

if __name__ == "__main__":
    obj = Tran('驴')
    obj.Run()