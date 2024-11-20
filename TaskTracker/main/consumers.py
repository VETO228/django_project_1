import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Принять WebSocket соединение

    async def disconnect(self, close_code):
        pass  # Обработка отключения

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Отправка уведомления обратно клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))