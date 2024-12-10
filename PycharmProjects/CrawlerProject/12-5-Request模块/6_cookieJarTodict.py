
import requests

url = 'http://www.baidu.com'
response = requests.get(url)
cookieJar = requests.utils.dict_from_cookiejar(response.cookies)

print(response.cookies)
print(cookieJar)
