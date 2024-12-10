import requests

url = 'https://sam.huat.edu.cn:8443/selfservive/'

response = requests.get(url,verify=False)

print(response.text)