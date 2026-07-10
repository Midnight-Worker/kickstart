import asyncio
from websockets.asyncio.server import serve


async def handler(websocket):
    print("Client verbunden")

    async for message in websocket:
        print("Empfangen:", message)

        antwort = f"Server sagt: Du hast '{message}' geschickt"
        await websocket.send(antwort)


async def main():
    async with serve(handler, "localhost", 8765):
        print("WebSocket-Server läuft auf ws://localhost:8765")
        await asyncio.Future()  # läuft für immer


asyncio.run(main())
