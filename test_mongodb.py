from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os 
from dotenv import load_dotenv

load_dotenv()

uri =os.getenv("MONGO_DB_URL")

client = MongoClient(
    uri,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where()
)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)