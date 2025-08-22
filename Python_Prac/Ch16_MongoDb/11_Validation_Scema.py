from pymongo import MongoClient
from datetime import datetime

myclient = MongoClient("mongodb://localhost:27017")

# Access database 
db = myclient.Sharydb

Schema={
    "bsontype":"object",
    "required":["id","Name","Age","Email","Date","Married"],
    "Prperties":{
        "id":{"bsonType":"Int","minimum":20},
        "Name":{"bsonType":"String"},
        "Email":{"bsonType":"String",'pattern': '^\\S+@\\S+\\.\\S+$'},
        "Date":{"bsonType":"date"},
        "Married":{"bsonType":"bool"}

    }
}

#Create collection 
collection=db.create_collection("Student",validator=Schema)

#Get validation information
print(collection.options())