from channels.generic.websocket import AsyncWebsocketConsumer
import json
from services.result import final_response_async
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

        complete_response=""

        async for chunk in final_response_async(query=message):
            complete_response=complete_response+chunk
            await self.send(text_data=json.dumps({
                        'type':'ai_response',
                        'message': chunk,
                    }))

        
        await ChatLogs.objects.acreate(user=self.user, query=message, answer=complete_response)

        await self.send(json.dumps({ 'type':'done' }))

    async def disconnect(self, code):
        print("client disconnected", code)





