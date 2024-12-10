import asyncio
import websockets
import json

async def send_question_response(question, response):
    """Send a question and response to the WebSocket server."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        
        message = json.dumps({"question": question, "response": response})
        await websocket.send(message)

        
        feedback = await websocket.recv()
        print("Feedback from server:", feedback)

async def main():
    """Main function to ask for user input and send it to the server."""
    print("Welcome to the AI Response Evaluation System!")
    
    while True:
        
        question = input("Please enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting the system.")
            break
        
        response = input("Please enter your response: ")

       
        await send_question_response(question, response)

if __name__ == "__main__":
    asyncio.run(main())
