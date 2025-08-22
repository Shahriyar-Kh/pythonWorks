import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.TutorialPoint

print("\n*************************** create index ******************** ")
idx=cln.create_index({"Name":1})
print("Idx is created")

print("\n*************************** Retreive index ******************** ")
idx_inf=cln.index_information()
for idx_name,idx_spec in idx_inf.items():
    print(f"idx_name: {idx_name}")
    print(f"idx_spec: {idx_spec}")


print("\n*************************** Drop index ******************** ")
cln.drop_index("Name_1")
print("Droped")
