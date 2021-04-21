from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url('chat/<room_name>', consumers.ChatConsumer),
]
