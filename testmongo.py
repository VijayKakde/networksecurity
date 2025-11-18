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
    
    # Check your specific database and collection
    # Replace these with YOUR actual database and collection names from your config
    database_name = "vijaydb"  # Update this with your actual database name
    collection_name = "NetworkData"  # Update this with your actual collection name
    
    print(f"\n--- Checking Database: {database_name} ---")
    db = client[database_name]
    print(f"Collections in {database_name}:", db.list_collection_names())
    
    print(f"\n--- Checking Collection: {collection_name} ---")
    collection = db[collection_name]
    doc_count = collection.count_documents({})
    print(f"Total documents in '{collection_name}': {doc_count}")
    
    if doc_count > 0:
        print(f"\nFirst document sample:")
        sample_doc = collection.find_one()
        print(sample_doc)
    else:
        print(f"\n⚠ WARNING: Collection '{collection_name}' is EMPTY!")
        print("This is why you're getting n_samples=0 error.")
        print("\nYou need to:")
        print("1. Upload data to this collection, OR")
        print("2. Change the collection name in your config to an existing collection with data")
    
except Exception as e:
    print(f"✗ Error: {e}")