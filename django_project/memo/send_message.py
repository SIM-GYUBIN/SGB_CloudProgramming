import requests
import json
from datetime import datetime

def send_kakao_message():
    from .models import Task

    tasks = Task.objects.all().order_by('-created_at')
    for task in tasks :
        current_time = datetime.now().time()
        task_time = task.time

        if current_time.hour == task_time.hour and current_time.minute == task_time.minute:
            with open("memo/kakao_code.json", "r") as fp:
                tokens = json.load(fp)

            friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

            headers = {"Authorization": "Bearer " + tokens["access_token"]}

            result = json.loads(requests.get(friend_url, headers=headers).text)

            print(type(result))
            print("=============================================")
            print(result)
            print("=============================================")
            friends_list = result.get("elements")
            print(friends_list)
            print("=============================================")
            print(friends_list[0].get("uuid"))
            friend_id = friends_list[0].get("uuid")
            print(friend_id)

            send_url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

            data = {
                'receiver_uuids': '["{}"]'.format(friend_id),
                "template_object": json.dumps({
                    "object_type": "text",
                    "text": f'{task.title}할 시간입니다!',
                    "link": {
                        "web_url": "www.daum.net",
                        "web_url": "www.naver.com"
                    },
                    "button_title": "바로 확인"
                })
            }
            task.is_notified = True
            task.save()

            response = requests.post(send_url, headers=headers, data=data)
            response.status_code

