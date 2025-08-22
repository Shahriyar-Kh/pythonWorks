from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
#access db
db=client.Sharydb
#Access collection
collection=db.TutorialPoint
print("\n****************************** Aggregation *****************************")

records_list=[{"$group":
               {}
               }
               ]