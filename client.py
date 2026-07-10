import asyncio
from websockets.asyncio.client import connect


async def main():
    uri = "ws://localhost:8765"

    async with connect(uri) as websocket:
        await websocket.send("Hallo Server!")

        antwort = await websocket.recv()
        print("Antwort:", antwort)


asyncio.run(main())
