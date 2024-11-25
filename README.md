# AI_Response_Evaluator
This project implements an AI-powered WebSocket-based system that evaluates the quality of student responses to AI-related questions in real-time. It uses a pre-trained machine learning model to evaluate the similarity between a given question and the response and provides feedback based on that evaluation.
# AI WebSocket Response Evaluation System

This project implements an AI-powered WebSocket-based system that evaluates the quality of student responses to AI-related questions in real-time. It uses a pre-trained machine learning model to evaluate the similarity between a given question and the response and provides feedback based on that evaluation.

## Tech Stack

- **Python 3.x**: The core language for this project.
- **WebSockets**: For establishing real-time communication between the client and server.
- **Redis**: Used for caching responses to optimize repeated queries.
- **Sentence-Transformers**: A library for transforming text into embeddings and calculating similarity scores using pre-trained models like `all-MiniLM-L6-v2`.
- **UnitTest**: For writing unit tests to verify the correctness of the logic.
  
## Folder Structure

```plaintext
AI_Response_Evaluator/
│
├── logic/                       # Core logic for response evaluation and caching
│   ├── __init__.py              # Marks the directory as a Python package
│   ├── cache.py                 # Caching-related logic (handles Redis caching)
│   ├── evaluator.py             # Logic to evaluate responses using Sentence-Transformer
│   └── logic.py                 # Main logic for processing question-response pairs
│
├── tests/                       # Unit tests for the project
│   └── test_logic.py            # Unit tests for response evaluation
│
├── websocket_server.py          # WebSocket server for handling incoming requests
├── websocket_client.py          # WebSocket client for sending questions and responses
├── requirements.txt             # Project dependencies
├── run.py                       # Script to start the WebSocket server
└── README.md              # Project documentation
```

### Files Overview

#### `websocket_server.py`
This file contains the WebSocket server logic that:
- Listens for incoming WebSocket connections.
- Processes incoming messages containing questions and responses.
- Evaluates the responses using the `analyze_response` function and sends back feedback.

#### `websocket_client.py`
This file contains the WebSocket client logic that:
- Prompts the user to input a question and response.
- Sends the question and response to the WebSocket server for evaluation.
- Receives and prints the feedback from the server.

#### `logic/`
This directory contains the core logic for the system:
- **`cache.py`**: Functions to interact with a Redis database for caching previously evaluated responses, improving performance for repeated requests.
- **`evaluator.py`**: Contains the logic for evaluating responses using the Sentence-Transformer model. It calculates a similarity score between the question and response.
- **`logic.py`**: The main file where the response analysis happens. It includes the `analyze_response` function, which checks for cached results, evaluates the response, and caches the result if necessary.

#### `tests/test_logic.py`
Contains unit tests for testing the functionality of the logic, particularly ensuring that valid and invalid responses are processed correctly.

---

## Installation

## Create and activate a virtual environment (Optional but recommended):
- python -m venv env
- env\Scripts\activate

## Install dependencies:
- pip install -r requirements.txt

## Install Redis (If not installed):
- On Windows: Download from Redis.io or use Memurai.

## Start Redis server (if not running):
- ./redis-server
  
## Running the Application
### Start the WebSocket server: 
- Open a terminal and run the following command to start the WebSocket server:
- python run.py

### Run the WebSocket client: 
- Open another terminal window and run the WebSocket client to start interacting with the system:
- python websocket_client.py

- The client will prompt you to input a question and a response, then send the data to the server. The server will evaluate the response and return a similarity score and feedback message.

## How It Works
WebSocket Communication:
- The WebSocket server (websocket_server.py) listens for incoming WebSocket connections.
- The client sends a JSON message containing a question and a response to the server.
- The server evaluates the response by checking the similarity between the question and response using the evaluate_response function in evaluator.py.
- The evaluation result, including a similarity score and feedback, is sent back to the client.
- Response Evaluation:
- The response evaluation is done using the Sentence-Transformer model (all-MiniLM-L6-v2), which is capable of generating embeddings for both the question and response, and then calculating the cosine similarity between them. Based on the similarity score, feedback is generated:

Similarity > 0.8: "Great answer!"
0.5 < Similarity <= 0.8: "Good attempt, but there's room for improvement."
Similarity <= 0.5: "Consider revisiting the topic for a better understanding."

Caching:
- To optimize performance, Redis is used to cache the results of previously evaluated question-response pairs. If the same pair is submitted again, the server will retrieve the cached result from Redis instead of re-evaluating the response.

Testing
- Unit tests are included to ensure that the response evaluation logic works correctly.

Run unit tests:
- python -m unittest discover tests


## Future Improvements
- Error handling: More robust error handling for edge cases like connection timeouts or invalid inputs.
- Enhanced Feedback: Expand feedback generation with more nuanced responses.
- Model Optimization: Experiment with different pre-trained models for better evaluation.
- User Interface: Build a front-end interface for a more interactive experience.

## Conclusion
This project provides a real-time, AI-based response evaluation system using WebSockets. It allows for the dynamic submission of questions and answers, evaluates the answers based on similarity, and provides feedback to help users improve their understanding of AI concepts. By utilizing caching and pre-trained models, it ensures both efficient performance and high-quality evaluations.
