from pymongo import MongoClient

# Replace with your MongoDB URL if needed
MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)
db = client["think41"]  # This is your database name
