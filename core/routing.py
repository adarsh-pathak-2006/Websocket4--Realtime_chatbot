from django.urls import path
from core.consumers import ChatBotConsumer


websocket_urlpatterns=[
    path('ws/cb/', ChatBotConsumer.as_asgi(), name='chatbot_consumer'),
]