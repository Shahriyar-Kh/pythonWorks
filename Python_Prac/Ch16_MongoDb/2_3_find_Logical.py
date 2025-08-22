from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")

#Access database 
db=myclient.Sharydb

#Access collection
collection=db.TutorialPoint


print("\n**************** Operators And *******************")
result2=collection.find({"$and":[{"Name":"Ysir"},{"Age":"20"}]})
for rows in result2:
    print(rows)

print("\n**************** Operators OR *******************")
result2=collection.find({"$or":[{"Name":"Shahriyar"},{"Age":"20"}]})
for rows in result2:
    print(rows)
print("\n**************** Operators nor *******************")
result2=collection.find({"$nor":[{"Age":{"$lte":22}},{"Age":{"$gte":26}}]})
for rows in result2:
    print(rows)

print("\n**************** Operators And,OR *******************")
result2=collection.find({"$and":[{"Name":"Shahriyar"},{"$or":[{"Age":"20"},{"City":"Swaat"}]}]})
for rows in result2:
    print(rows)

print("\n**************** Operators not *******************")
# result2=collection.find({"$not":[{"Name":"Shahriyar"},{"Age":"20"}]})
# for rows in result2:
#     print(rows)

