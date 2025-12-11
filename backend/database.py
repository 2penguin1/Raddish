from pymongo import MongoClient
import os

# Connect to local MongoDB
# In production, use env var: os.getenv("MONGO_URI")
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "cf_predictor"

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        try:
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
            self.db = self.client[DB_NAME]
            # Verify connection
            self.client.server_info()
            print("Connected to MongoDB.")
        except Exception as e:
            print("Warning: Could not connect to MongoDB. Running in offline/memory mode.")
            self.client = None

    def get_user(self, handle):
        if not self.client: return None
        return self.db.users.find_one({"handle": handle.lower()})

    def update_user(self, handle, data):
        if not self.client: return
        self.db.users.update_one(
            {"handle": handle.lower()}, 
            {"$set": data}, 
            upsert=True
        )

    def log_prediction(self, handle, prediction_data):
        if not self.client: return
        self.db.predictions.insert_one({
            "handle": handle.lower(),
            "timestamp": prediction_data.get("timestamp"),
            "predicted_rating": prediction_data.get("predicted_rating"),
            "delta": prediction_data.get("delta")
        })

    def get_contest_data(self):
        # Fetch sequential contest data for training
        if not self.client: return []
        return list(self.db.contests.find().sort("startTimeSeconds", 1))

db = Database()
