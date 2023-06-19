import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '35260dcf52135612834d1b3c3ccd3f64'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'WX3hfOLWPRRJgWM5OSnSGwsBOSYkgfADh4HKwSeawdKBuN3kXR2z3aeeQ4To_W7SvynM0Ao9c-wAAAGIzrs4Yg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)

# json 읽어오기
# import json
# #1.
# with open(r"C:\django_workspace\SGB_CloudProgramming\django_project\memo\kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])