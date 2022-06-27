import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phones_backend.settings')

app = Celery('phones_backend',)


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = 'redis://192.168.0.104:6379/0'
app.conf.result_backend = 'redis://192.168.0.104:6379/1'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
