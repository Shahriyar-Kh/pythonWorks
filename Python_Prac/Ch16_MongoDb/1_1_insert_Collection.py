from pymongo import MongoClient
import datetime

#Connection
client=MongoClient("mongodb://localhost:27017")

#Access db
db=client.Sharydb

#Access or create Collection or table
collection=db["Post"]

records=[
    {
        "title":"Mogodb overview",
        "Description":"Mogodb is no SQL database",
        "By":"Tutorials point",
        "URl":"http://www.tutorialspoint.com",
        "Tages":["Mongodb","Database","NoSQL"],
        "Likes":100
    },
    {
    "Title":"NoSQL Database",
    "Description":"NoSQL Database Doesn,t have tables",
    "By":"Tutorial point",
    "Tages":["Mongodb","Database","NoSQL"],
    "Likes":100,
    "URl":"http://www.tutorialspoint.com",
    "Comments":[
        {
            "User":"User1",
            "Message":"My first Comment",
            "DateCreated":datetime.datetime(2024,11,10,2,35),
            "Like":0,
        }]
}]

result=collection.insert_many(records)

