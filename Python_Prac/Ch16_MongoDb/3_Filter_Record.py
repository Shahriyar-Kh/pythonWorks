import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.Customer

print("\n*************** Find document(s) by address *************** ")
finding={"Address":"Charsadda"}
result=cln.find(finding)

for records in result:
    print(records)

print("\n*************** Find document(s) by address start letter *************** ")
#Find documents where the address starts with the letter "S" or higher:

finding1={"Address":{"$gt":"P"}}
result1=cln.find(finding1)
for records in result1:
    print(records)

print("\n*************** Find document(s) using Regression Exp *************** ")
finding2={"Address":{"$regex":"^P"}}
result2=cln.find(finding2)
for record in result2:
    print(record)

