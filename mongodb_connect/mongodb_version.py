from pymongo import MongoClient
import os

mongoconnector = os.environ.get('mongoconnector')

# Connect to the MongoDB server
# client = MongoClient("mongodb://localhost:27017/")  # Update the URL if using a remote server
client = MongoClient(mongoconnector)

# Get server information
server_info = client.server_info()

# Print the MongoDB version
print(f"MongoDB Version: {server_info['version']}")
