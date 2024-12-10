import asyncio
import websockets
import json
import logging
from logic.logic import analyze_response

logging.basicConfig(level=logging.INFO)

async def handle_client(websocket, path):
   
    logging.info(f"Connected to {websocket.remote_address}")
    
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                question = data.get("question")
                response = data.get("response")

                if not question or not response:
                    await websocket.send(json.dumps({"error": "Both question and response are required."}))
                    continue

                result = analyze_response(question, response)
                await websocket.send(json.dumps(result))

            except json.JSONDecodeError:
                await websocket.send(json.dumps({"error": "Invalid JSON format."}))

    except websockets.ConnectionClosed:
        logging.info(f"Connection closed with {websocket.remote_address}")
    except Exception as e:
        logging.error(f"Error: {e}")

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        logging.info("WebSocket server running at ws://localhost:8765")
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())
