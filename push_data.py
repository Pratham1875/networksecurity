import os
import sys

import certifi
import pandas as pd
import pymongo

from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Certificate authority
ca = certifi.where()


class NetworkDataExtract:

    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Convert CSV data into JSON-like records
    def csv_to_json_converter(self, file_path):

        try:
            data = pd.read_csv(file_path)

            # Reset index
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame to list of dictionaries
            records = data.to_dict(orient="records")

            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Insert records into MongoDB
    def insert_data_mongodb(self, records, database, collection):

        try:

            # Create MongoDB client
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=ca
            )

            # Select database
            self.database = self.mongo_client[database]

            # Select collection
            self.collection = self.database[collection]

            # Insert records
            self.collection.insert_many(records)

            # Return number of records inserted
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    # CSV file path
    FILE_PATH = "Network_Data/phisingData.csv"

    # MongoDB database
    DATABASE = "PRATHAMAI"

    # MongoDB collection
    COLLECTION = "NetworkData"

    # Create object
    networkobj = NetworkDataExtract()

    # Convert CSV to records
    records = networkobj.csv_to_json_converter(
        file_path=FILE_PATH
    )

    print("Number of records read from CSV:", len(records))

    # Insert records into MongoDB
    no_of_records = networkobj.insert_data_mongodb(
        records,
        DATABASE,
        COLLECTION
    )

    print("Number of records inserted:", no_of_records)

    print("Data inserted successfully into MongoDB!")