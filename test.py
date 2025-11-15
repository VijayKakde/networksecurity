import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

try:
    client = pymongo.MongoClient(MONGO_DB_URL, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✓ Connection successful!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print(f"✗ Connection failed: {e}")