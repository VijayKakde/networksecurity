import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records
            
            # Use the EXACT same connection pattern that worked in test
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                serverSelectionTimeoutMS=5000
            )
            
            # Test connection
            self.mongo_client.admin.command('ping')
            print("✓ Connected to MongoDB successfully!")
            
            # Access database and collection
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]
            
            # Insert records
            result = self.collection.insert_many(self.records)
            
            print(f"✓ Inserted {len(result.inserted_ids)} records into {database}.{collection}")
            
            return len(result.inserted_ids)
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        finally:
            # Close connection
            if hasattr(self, 'mongo_client'):
                self.mongo_client.close()
        
if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "vijaydb"
    Collection = "NetworkData"
    
    try:
        networkobj = NetworkDataExtract()
        
        # Convert CSV to JSON
        print("Converting CSV to JSON...")
        records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
        print(f"✓ Total records converted: {len(records)}")
        
        # Insert into MongoDB
        print("Inserting data into MongoDB...")
        no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
        print(f"✓ Successfully inserted {no_of_records} records!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        raise
