from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")

#Access database 
db=myclient.Sharydb

#Access collection
cust_cln=db.Customer

print("\n**************** Find one() ****************")
result=cust_cln.find_one()
print(result)

print("\n**************** Find() all record  ****************")
result=cust_cln.find()

for i in result:
    print(i)


print("\n**************** names and addresses ****************")

for data in cust_cln.find({},{"_id":0,"name":1,"address":1}):
    print(data)

print("\n**************** Exclude address ****************")
for data in cust_cln.find({},{"address":0}):
    print(data)
