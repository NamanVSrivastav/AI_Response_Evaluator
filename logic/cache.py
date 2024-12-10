import redis
import json
import logging


try:
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()
    redis_available = True
except redis.ConnectionError:
    logging.warning("Redis is unavailable. Using in-memory fallback cache.")
    redis_client = None
    redis_available = False

memory_cache = {}

def get_cached_result(cache_key):
    if redis_available:
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return json.loads(cached_result)
    return memory_cache.get(cache_key)

def cache_result(cache_key, result):
   
    if redis_available:
        redis_client.set(cache_key, json.dumps(result), ex=3600)  # Cache for 1 hour
    else:
        memory_cache[cache_key] = result
