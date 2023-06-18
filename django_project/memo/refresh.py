def refresh():
    import requests
    import json
    url = "https://kauth.kakao.com/oauth/token"
    data = {
    "grant_type" : "refresh_token",
    "client_id" : "35260dcf52135612834d1b3c3ccd3f64",
    "refresh_token" : "ukpLSLFBizFpQDVQnDLyfTqqqCaM0NzAuBIM8HGqCj11GgAAAYjJxfyG"
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    # print(response.json())

    with open("memo/kakao_code.json","w") as fp:
        json.dump(tokens, fp)
