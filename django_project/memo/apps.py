from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig
from datetime import datetime
from pytz import timezone
from .send_message import send_kakao_message
from .refresh import refresh

class MemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memo'

    def ready(self):
        from .send_message import send_kakao_message

        scheduler = BackgroundScheduler()
        #scheduler.add_job(send_kakao_message, 'interval', minutes=1)  # 예시: 1분마다 실행
        scheduler.add_job(refresh, 'interval', hours=6)  # 예시: 1분마다 실행
        scheduler.start()