import unittest
from logic.logic import analyze_response

class TestLogic(unittest.TestCase):

    def test_valid_response(self):
        question = "What is AI?"
        response = "AI stands for Artificial Intelligence."
        result = analyze_response(question, response)
        self.assertIn("similarity", result)
        self.assertIn("feedback", result)

    def test_empty_response(self):
        with self.assertRaises(ValueError):
            analyze_response("What is AI?", "")

    def test_empty_question(self):
        with self.assertRaises(ValueError):
            analyze_response("", "AI is Artificial Intelligence.")

if __name__ == "__main__":
    unittest.main()
