from channels.generic.websocket import AsyncWebsocketConsumer
import json
from services.result import final_response
from asgiref.sync import sync_to_async
from core.models import ChatLogs

class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope["user"]
        if self.user.is_authenticated:
            print("connection enstablished")
            await self.accept()
        else:
            await self.close()

    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data.get("message")

        ai_response=await sync_to_async(final_response)(query=message)

        ai=json.dumps({
            'type':'ai_response',
            'message': ai_response,
        })
        await ChatLogs.objects.acreate(user=self.user, query=message, answer=ai_response)

        await self.send(text_data=ai)

    async def disconnect(self, code):
        print("client disconnected", code)





