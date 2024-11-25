import asyncio
import websockets
import json

async def send_question_response(question, response):
    """Send a question and response to the WebSocket server."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Send the question and response as JSON to the server
        message = json.dumps({"question": question, "response": response})
        await websocket.send(message)

        # Receive feedback from the server
        feedback = await websocket.recv()
        print("Feedback from server:", feedback)

async def main():
    """Main function to ask for user input and send it to the server."""
    print("Welcome to the AI Response Evaluation System!")
    
    while True:
        # Ask for question input
        question = input("Please enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting the system.")
            break
        
        # Ask for response input
        response = input("Please enter your response: ")

        # Send the question and response to the WebSocket server
        await send_question_response(question, response)

if __name__ == "__main__":
    asyncio.run(main())
