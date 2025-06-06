from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "worker",
    # Redis連接
    broker="redis://localhost:6379/0",
    # 後端
    backend="redis://localhost:6379/0",
    # 任務模組
    include=["app.tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Taipei",
    enable_utc=False,
)

celery_app.conf.beat_schedule = {
    "write_log_everyday": {
        "task": "app.tasks.log_current_now_time",
        "schedule": crontab(hour=9, minute=0),
    },
    "write_log_every_minute": {
        "task": "app.tasks.log_current_now_time",
        "schedule": crontab(minute="*")
    },
}