import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")


#Access database
db=client.Sharydb

#Create Colection
collection=db["TutorialPoint"]

print("\n******************** $inc using ***************************")
result=collection.update_many({},{"$inc":{"Age":2}})

for doc in collection.find():
    print("Increase the age by 2:",doc)
print("\n******************** $max using ***************************")
result=collection.update_one({"Name":"Mobeen"},{"$max":{"Age":50}})
for doc in collection.find():
    print("increase age of the Shayan :",doc)

print("\n******************** $min using ***************************")
result=collection.update_one({"Name":"Shahriyar"},{"$min":{"Age":10}})
for doc in collection.find():
    print("increase age of the Shayan :",doc)

print("\n******************** $min using ***************************")
result=collection.update_one({"Name":"Shahriyar"},{"$min":{"Age":10}})
for doc in collection.find():
    print(doc)

print("\n******************** $mul using ***************************")
result=collection.update_one({"Name":"Shahriyar"},{"$mul":{"Age":2}})
for doc in collection.find():
    print(doc)

print("\n******************** $unset using ***************************")
result=collection.update_one({"Name":"Ali"},{"$unset":{"Age":22222}})
for doc in collection.find():
    print(doc)

print("\n******************** $rename using ***************************")
result=collection.update_many({},{"$rename":{"Age":"StudentAge"}})
for doc in collection.find():
    print(doc)





