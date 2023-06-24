from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig
from datetime import datetime, timedelta
from pytz import timezone
from .send_message import send_kakao_message
from .refresh import refresh

class MemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memo'

    def ready(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(refresh, 'interval', minutes=5, start_date=datetime.now() + timedelta(seconds=1))
        scheduler.start()