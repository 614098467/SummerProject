import requests

url = 'http://www.baidu.com'

proxies = {
    "http":"183.238.163.8:9002"
}

response = requests.post(url,proxies = proxies)

print(response.status_code)