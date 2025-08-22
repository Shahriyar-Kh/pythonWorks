from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")

#Access database 
db=myclient.Sharydb

#Access collection
collection=db.TutorialPoint



    
print("\n**************** Operators (Equality) using $eq ***********************")
for row in collection.find({"Name":{"$eq":"Shahriyar"}}):
    print(row)

print("\n**************** Operators (Equality) using $ne ***********************")
for row in collection.find({"Name":{"$ne":"Shahriyar"}}):
    print(row)

print("\n**************** Operators (less than) ***********************")
for row in collection.find({"Age":{"$lt":"22"}}):
    print(row)

print("\n**************** Operators (less than or Equals) *******************")
for row in collection.find({"Age":{"$lte":"22"}}):
    print(row)


print("\n**************** Operators (grater than ) *******************")
for row in collection.find({"Age":{"$gt":"29"}}):
    print(row)

print("\n**************** Operators (grater than or equals ) *******************")
for row in collection.find({"Age":{"$gte":"29"}}):
    print(row)

print("\n**************** Operators $in *******************")
result2=collection.find({"Age":{"$in":["20","29"]}})
for row in result2:
    print(row)

print("\n**************** Operators $nin *******************")
result2=collection.find({"Age":{"$nin":["20","29"]}})
for row in result2:
    print(row)