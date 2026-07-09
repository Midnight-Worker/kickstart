import asyncio
from websockets.asyncio.server import serve


PORT = 8765


async def handle_client(websocket):
    print("Client verbunden")

    await websocket.send("Willkommen vom Python WebSocket Server!")

    async for message in websocket:
        print("Nachricht:", message)
        await websocket.send(f"Echo: {message}")


async def main():
    async with serve(handle_client, "localhost", PORT):
        print(f"WebSocket Server läuft auf ws://localhost:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
