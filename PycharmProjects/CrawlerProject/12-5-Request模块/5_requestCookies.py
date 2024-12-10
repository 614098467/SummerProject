import requests

url = 'https://github.com/614098467'

headersWithoutCookie = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

cookiesContent ='_device_id=9dac6d4e438d07f1318b4857e3d601f9; _octo=GH1.1.1072104782.1720286276; cpu_bucket=xlg; preferred_color_mode=dark; tz=Asia%2FShanghai; saved_user_sessions=44646821%3AgA4rrPm2dFt_PjY6IWSQJLTiw1EPfMdpNRFMMqMAN90S_3eP; user_session=gA4rrPm2dFt_PjY6IWSQJLTiw1EPfMdpNRFMMqMAN90S_3eP; __Host-user_session_same_site=gA4rrPm2dFt_PjY6IWSQJLTiw1EPfMdpNRFMMqMAN90S_3eP; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=614098467; _gh_sess=haQoL9rQDxDxny7Vz6idVw6UMzuhYO3vhXGKPZEzY7eWMIyjan6zNFX5p7KQcg%2B68TzlPvWmuQJ1OWo2rhKE%2FiB2ipX2bdxsDcEPjzsFaMvyDJnCq7%2BbheaE9vHcsldkPUKQNAusuIwfwmwSiAvfuGp0D7T0KFqjVs9LN14e23%2BsIm03u5hF8OlKYnfC0nfAO1ehLaM12Jp%2FM92JZiC0LCK2rxpfwxTsuC5CvJp%2FVjF2VdzLaG6dK9SrB%2F%2FHnyeLxd0cDDw2k5YXenmSZeopwa4yNBpwFtV8bzY4bCrW%2BL8jvYYuFpkeHmjz6b%2FTh4mBjPGhKHeGjYSVz25EbfcSXKoQM%2FSMNk6xIHjZXz5OjM9o4vNls3Qllk1fYce%2FSjgDB2Bh1UGB5f4zoJ%2FoPgp2Oatn%2F%2BUk55MPS6%2BcizQVlz6udaAwyKo%2Ff7TkMeugHhjMnsThfS1qoouLLTau6TEbJXF7fwvxS4sBbjrnjG2rKmsh0Pb3%2BRqNAUZ1rBNFPxxzEBBUcTPiXEukE9mjfvCbllIQvHN83LzH1fJ%2FJmS1Z7%2Fz%2BiU9iVNQeqaKEIGm0shi1nmcHo0tn1YZU3VtbtUumnfgdmuYZRtJ7iKK%2BkWLOpq62vIuDd9RskeTSONPvsXZIlpG7mKVxpXv0LTukbbKEJKkZGPtj%2F%2FJP8x%2BWz6YLSbxHuRvHk2BJdJ3f5PHZ%2Fn5LrfkhQ%2FQB4CTrFTNWiSidbxDCJKqFXij46w6sx%2BWfQZogjNnls46lj6VcnN2qwER3aUIUg%2B5GxMab8Motv7j9fhJV1yDcyiH9qglauCEDejBBRH6tZCaM1DanOZMX%2B%2BO3CbNSQhLqKjviLZ9419x8lD%2FRHF1GjezJYU%2F1uE%2FjrQS93W%2B--50pLOEALIeYCYw4%2B--PpGJ4Q1lLFunMu%2BQYXcyDw%3D%3D'

cookieList = cookiesContent.split('; ')

cookies = {cookies.split('=')[0]:cookies.split('=')[-1] for cookies in cookieList}

print(cookies)

response = requests.get(url,headers=headersWithoutCookie,cookies=cookies)

with open('5_requestCookies.html','wb') as f:
    f.write(response.content)



