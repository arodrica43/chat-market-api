from typing import Optional

from fastapi import FastAPI

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection

app = FastAPI()


@app.get("/")
async def root():
    try:
        client.admin.command('ping')
        return {"message": "Pinged your deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        return {"message": e}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
