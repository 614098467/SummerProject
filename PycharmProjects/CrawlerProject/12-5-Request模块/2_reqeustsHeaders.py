
import  requests

url = 'http://www.baidu.com'

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response1 = requests.get(url,headers = headers)
print(response1.content.decode('utf-8'))
print(len(response1.content.decode('utf8')))

