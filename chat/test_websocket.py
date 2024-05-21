import asyncio
import websockets
import json

async def test_chat():
    uri = "ws://127.0.0.1:8000/ws/chat/chatik/"
    async with websockets.connect(uri) as websocket:
        message = {
            "message": "Hello, World!"
        }
        await websocket.send(json.dumps(message))
        
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(test_chat())
