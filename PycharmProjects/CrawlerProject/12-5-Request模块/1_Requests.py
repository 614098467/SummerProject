
import requests

url = 'http://www.baidu.com'
response = requests.get(url)
# 源码的str类型的数据
print('Url:',response.url)
print('Status_code:',response.status_code)
print('Headers:',response.headers)
print('Request headers:',response.request.headers)
print('Request Cookie:',response.cookies)
