from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")

#Access database 
db=myclient.Sharydb

#Access collection
collection=db.TutorialPoint

print("\n**************** FindOne() one row ***********************")
result=collection.find_one()
print(result)

print("\n**************** Find() multiple rows ***********************")
result1=collection.find()
for rows in result1:
    print(rows)
print("\n**************** Find() by column ***********************")
result1=collection.find({},{"Name":1,"_id":0})
for rows in result1:
    print(rows)




print("\n**************** Operators And *******************")
result2=collection.find({"$and":[{"Name":"Shahriyar"},{"Age":"30"}]})
for rows in result2:
    print(rows)

print("\n**************** Operators OR *******************")
result2=collection.find({"$or":[{"Name":"Shahriyar"},{"Age":"20"}]})
for rows in result2:
    print(rows)

print("\n**************** Operators And,OR *******************")
result2=collection.find({"$and":[{"Name":"Shahriyar"},{"$or":[{"Age":"20"},{"City":"Swaat"}]}]})
for rows in result2:
    print(rows)

print("\n**************** Operators not *******************")
# result2=collection.find({"$Not":[{"Name":"Shahriyar"},{"Age":"20"}]})
# for rows in result2:
#     print(rows)

