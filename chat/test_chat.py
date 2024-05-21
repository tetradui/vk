import asyncio
import websockets
import json

async def test_chat():
    uri = "ws://127.0.0.1:8000/ws/chat/<room_name>/"  # Замените <room_name> на имя вашей комнаты
    async with websockets.connect(uri) as websocket:
        # Отправка сообщения
        message = {
            "message": "Hello, World!",
            "username": "user1",
            "room": "<room_name>"  # Замените <room_name> на имя вашей комнаты
        }
        await websocket.send(json.dumps(message))
        
        # Получение сообщения
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(test_chat())
