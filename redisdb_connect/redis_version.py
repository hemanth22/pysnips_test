import redis
import os

# Replace with your Redis connection details
redis_host = os.environ.get('redis_host')
redis_port = os.environ.get('redis_port')
redis_password = os.environ.get('redis_password')
redis_username = os.environ.get('redis_username')

# Connect to the Redis server with authentication
redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    username=redis_username,
    password=redis_password,
    decode_responses=True
)

# Get the Redis server information
try:
    info = redis_client.info()
    redis_version = info.get("redis_version")
    print(f"Redis version: {redis_version}")
except redis.AuthenticationError:
    print("Authentication failed: Check your username and password.")
except Exception as e:
    print(f"An error occurred: {e}")
