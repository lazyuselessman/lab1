from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws', consumers.PhoneConsumer.as_asgi()),
]