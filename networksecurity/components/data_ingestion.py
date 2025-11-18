from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


## configuration of the Data Ingestion Config

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        """
        Read data from mongodb
        """
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            
            logging.info(f"=" * 60)
            logging.info(f"Starting MongoDB data export")
            logging.info(f"Database: {database_name}")
            logging.info(f"Collection: {collection_name}")
            logging.info(f"MongoDB URL configured: {MONGO_DB_URL is not None}")
            
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]
            
            # Check document count
            doc_count = collection.count_documents({})
            logging.info(f"Total documents in MongoDB collection: {doc_count}")
            
            if doc_count == 0:
                raise ValueError(f"No documents found in collection '{collection_name}' of database '{database_name}'")
            
            # Fetch all documents
            logging.info(f"Fetching documents from MongoDB...")
            documents = list(collection.find())
            logging.info(f"Successfully fetched {len(documents)} documents")
            
            # Create DataFrame
            df = pd.DataFrame(documents)
            logging.info(f"DataFrame created - Shape: {df.shape}")
            logging.info(f"DataFrame columns: {df.columns.tolist()}")
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
                logging.info(f"Dropped '_id' column - New shape: {df.shape}")
            
            # Check for missing values before replacement
            logging.info(f"DataFrame info before 'na' replacement:")
            logging.info(f"  - Total rows: {len(df)}")
            logging.info(f"  - Total columns: {len(df.columns)}")
            
            df.replace({"na": np.nan}, inplace=True)
            
            logging.info(f"Final DataFrame shape: {df.shape}")
            logging.info(f"DataFrame head:\n{df.head()}")
            logging.info(f"=" * 60)
            
            return df
            
        except Exception as e:
            logging.error(f"Error in export_collection_as_dataframe: {str(e)}")
            raise NetworkSecurityException(e, sys)
        
    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            logging.info(f"Exporting data to feature store")
            logging.info(f"Input DataFrame shape: {dataframe.shape}")
            
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            
            # Creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Created directory: {dir_path}")
            
            # Save to CSV
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Data exported to: {feature_store_file_path}")
            
            # Verify file was created
            if os.path.exists(feature_store_file_path):
                file_size = os.path.getsize(feature_store_file_path)
                logging.info(f"File created successfully - Size: {file_size} bytes")
            
            logging.info(f"Returning DataFrame with shape: {dataframe.shape}")
            return dataframe
            
        except Exception as e:
            logging.error(f"Error in export_data_into_feature_store: {str(e)}")
            raise NetworkSecurityException(e, sys)
        
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            logging.info(f"=" * 60)
            logging.info(f"Starting train-test split")
            logging.info(f"Input DataFrame shape: {dataframe.shape}")
            logging.info(f"DataFrame type: {type(dataframe)}")
            logging.info(f"DataFrame is None: {dataframe is None}")
            logging.info(f"DataFrame length: {len(dataframe)}")
            
            # Critical validation
            if dataframe is None:
                raise ValueError("DataFrame is None!")
            
            if len(dataframe) == 0:
                raise ValueError(f"DataFrame is empty! Shape: {dataframe.shape}")
            
            logging.info(f"Split ratio: {self.data_ingestion_config.train_test_split_ratio}")
            
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            
            logging.info(f"Split completed successfully")
            logging.info(f"Train set shape: {train_set.shape}")
            logging.info(f"Test set shape: {test_set.shape}")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Saving train set to: {self.data_ingestion_config.training_file_path}")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )
            
            logging.info(f"Saving test set to: {self.data_ingestion_config.testing_file_path}")
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )
            
            logging.info(f"Train and test files exported successfully")
            logging.info(f"=" * 60)
            
        except Exception as e:
            logging.error(f"Error in split_data_as_train_test: {str(e)}")
            raise NetworkSecurityException(e, sys)
        
        
    def initiate_data_ingestion(self):
        try:
            logging.info(f"\n{'=' * 60}")
            logging.info(f"STARTING DATA INGESTION PIPELINE")
            logging.info(f"{'=' * 60}\n")
            
            # Step 1: Export from MongoDB
            logging.info(f"STEP 1: Exporting data from MongoDB")
            dataframe = self.export_collection_as_dataframe()
            logging.info(f"✓ MongoDB export completed - DataFrame shape: {dataframe.shape}\n")
            
            # Step 2: Save to feature store
            logging.info(f"STEP 2: Saving to feature store")
            dataframe = self.export_data_into_feature_store(dataframe)
            logging.info(f"✓ Feature store export completed - DataFrame shape: {dataframe.shape}\n")
            
            # Step 3: Split into train and test
            logging.info(f"STEP 3: Splitting into train and test sets")
            self.split_data_as_train_test(dataframe)
            logging.info(f"✓ Train-test split completed\n")
            
            # Create artifact
            dataingestionartifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            
            logging.info(f"{'=' * 60}")
            logging.info(f"DATA INGESTION COMPLETED SUCCESSFULLY")
            logging.info(f"Train file: {dataingestionartifact.trained_file_path}")
            logging.info(f"Test file: {dataingestionartifact.test_file_path}")
            logging.info(f"{'=' * 60}\n")
            
            return dataingestionartifact

        except Exception as e:
            logging.error(f"\n{'=' * 60}")
            logging.error(f"DATA INGESTION FAILED")
            logging.error(f"Error: {str(e)}")
            logging.error(f"{'=' * 60}\n")
            raise NetworkSecurityException(e, sys)