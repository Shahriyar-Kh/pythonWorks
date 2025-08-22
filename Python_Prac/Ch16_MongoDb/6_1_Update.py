import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.TutorialPoint

print("\n*************** Print all records ***********************")
records=cln.find()
for rows in records:
    print(rows)

print("\n************************ findOneAndUpdate() using ***************************")
result=cln.find_one_and_update(
    {"Name":"Shahriyar"},
    {"$set":{"Age":"24","Email":"shahriyarkhanpk1@gmail.com"}}
)
records=cln.find()
for rows in records:
    print(rows)