from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_response(question, response):
 
    if not question or not response:
        raise ValueError("Question and response cannot be empty.")
    
  
    question_embedding = model.encode(question, convert_to_tensor=True)
    response_embedding = model.encode(response, convert_to_tensor=True)

  
    similarity = util.pytorch_cos_sim(question_embedding, response_embedding).item()

  
    if similarity > 0.8:
        feedback = "Great answer!"
    elif similarity > 0.5:
        feedback = "Good attempt, but there's room for improvement."
    else:
        feedback = "Consider revisiting the topic for a better understanding."

    return {"similarity": similarity, "feedback": feedback}
