from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создайте экземпляр Celery
app = Celery('pythonProject1')

# Загрузите настройки из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживайте задачи (tasks) в приложениях
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
