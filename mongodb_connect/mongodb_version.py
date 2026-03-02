from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

mongoconnector = os.environ.get('mongoconnector')

# Use the connection string from environment variable
uri = mongoconnector if mongoconnector else "mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    
    # Get server information
    server_info = client.server_info()
    
    # Print the MongoDB version
    print(f"MongoDB Version: {server_info['version']}")
except Exception as e:
    print(f"Connection error: {e}")
finally:
    client.close()
