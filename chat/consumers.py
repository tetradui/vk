import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Message
from django.conf import settings
from asgiref.sync import sync_to_async

User = settings.AUTH_USER_MODEL

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        user = await sync_to_async(User.objects.get)(username=username)
        chat = await sync_to_async(Chat.objects.get)(id=room)
        message = await sync_to_async(Message.objects.create)(user=user, content=message)
        await sync_to_async(chat.messages.add)(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'username': user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
