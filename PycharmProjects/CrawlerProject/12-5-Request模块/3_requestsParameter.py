



import  requests

''' 
Method1: 
'''

# url = 'http://www.baidu.com/s?wd=python'
#
# headers = {
#     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
# }
# response = requests.get(url,headers = headers)
#
# with open('baidu.html','wb') as f:
#     f.write(response.content)

'''
 Method2:
'''

url = 'http://www.baidu.com/s?'
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
data = {
    'wd':'秦岭野生动物园'
}
response2  = requests.get(url,headers = headers,params=data)
with open('秦岭野生动物园.html','wb') as f:
    f.write(response2.content)





