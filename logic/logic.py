from functools import lru_cache
from logic.cache import get_cached_result, cache_result
from logic.evaluator import evaluate_response

@lru_cache(maxsize=100)
def analyze_response(question, response):
    """Analyze a student's response using caching and evaluation."""
    cache_key = f"{question}_{response}"
    
    # Check cached result
    cached_result = get_cached_result(cache_key)
    if cached_result:
        return cached_result

    # Evaluate the response
    result = evaluate_response(question, response)

    # Cache the result
    cache_result(cache_key, result)

    return result
