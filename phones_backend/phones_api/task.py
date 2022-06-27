from celery import shared_task
import time

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from datetime import datetime

from phones_api.models import Phone

@shared_task()
def calculate_numbers():
    user_numbers_count = {}
    for phone in Phone.objects.all():
        user_numbers_count[phone.surname] = len(phone.numbers.all())
    
    print(user_numbers_count)

    # simulating long task
    time.sleep(3)
    async_to_sync(get_channel_layer().group_send)(
        "common",
        {
            "type": "calculate_numbers",
            "completedTask": {
                "name": "calculate_numbers",
                "data": "None",
                "result": None,
                "endDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        }
    )