from pymongo import MongoClient
from datetime import datetime

myclient = MongoClient("mongodb://localhost:27017")

# Access database 
db = myclient.Sharydb

# Access collection
collection = db.TutorialPoint

# Insert document with different data types
collection.insert_one({
    "Name": "Hamad",
    "isFounded": True,
    "Founding": 345678,
    "Employees": [
        {"Name": "Yaseen", "age": 24},
        {"Name": "Juniad", "age": 25}
    ],
    "foundedOn": datetime.now(),
    "Fondedontimestamp": datetime.now()
})
x=collection.find({"Name":"Hamad","_id":0})
for docs in x:
    print(docs)