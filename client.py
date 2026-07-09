import asyncio
from websockets.asyncio.client import connect


async def main():
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hallo Server")

        response = await websocket.recv()
        print(response)


asyncio.run(main())
