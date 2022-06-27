import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from phones_api.task import calculate_numbers

class PhoneConsumer(WebsocketConsumer):
    common_group_name = "common"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.common_group_name,
            self.channel_name
        )
        print(f'Connected {self.channel_name}')
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        print(f'Disconnected {self.channel_name}')
        async_to_sync(self.channel_layer.group_discard)(
            self.common_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(f'phones-backend receive: Received {data}')

        if data["type"] == "number_add":
            async_to_sync(self.channel_layer.group_send)(
                self.common_group_name,
                {
                    "type": "number_add",
                }
            )
        elif data["type"] == "number_update":
            async_to_sync(self.channel_layer.group_send)(
                self.common_group_name,
                {
                    "type": "number_update",
                }
            )
        elif data["type"] == "number_delete":
            async_to_sync(self.channel_layer.group_send)(
                self.common_group_name,
                {
                    "type": "number_delete",
                }
            )
        elif data["type"] == "calculate_numbers":
            calculate_numbers.apply_async(queue="long_time_task")

    def number_add(self, event):
        print(f'Send number_add')
        self.send(text_data=json.dumps(event))

    def number_update(self, event):
        print(f'Send number_update')
        self.send(text_data=json.dumps(event))

    def number_delete(self, event):
        print(f'Send delete')
        self.send(text_data=json.dumps(event))

    def calculate_numbers(self, event):
        print(f'calculate numbers')
        self.send(text_data=json.dumps(event))
