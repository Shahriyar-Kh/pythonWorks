import pymongo

mclient=pymongo.MongoClient("mongodb://localhost:27017")
#Access the database 
db=mclient.Sharydb

#Access Collection or table
CustColection=db.Customer

#Insert a record 
dict={"Id":1,"name":"Shary","Address":"Charsadda"}
x=CustColection.insert_one(dict)
print(x)

#Example Insert another record in the "customers" collection, and return the value of the _id field:
print("\n******************* Example2 Insert one record ***********")
dict1={"Name":"Umair","Address":"Peshawer"}
x2=CustColection.insert_one(dict1)
print(x2.inserted_id)

print("\n******************* Example2 Insert many record with specified ids ***********")
record_list=[
    {"_id":4,"Name":"Fahad","Address":"Mardan"},
    {"_id":5,"Name":"Ali","Address":"Swat"},
    {"_id":6,"Name":"Shary","Address":"Umerzai"},
    {"_id":7,"Name":"Hamza","Address":"Peshawer"},
    {"_id":8,"Name":"Hamad","Address":"Charsadda"},
    
]

x3=CustColection.insert_many(record_list)
#print list of the all id values of the inserted doc
print(x3.inserted_ids)