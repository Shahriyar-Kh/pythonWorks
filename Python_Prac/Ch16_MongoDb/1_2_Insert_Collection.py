import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")


#Access database
db=client.Sharydb

#Create Colection
collection=db["TutorialPoint"]

records=[
    {"_id":1001,"Name":"Shayan","Age":22,"City":"Peshawer","Bio":"I am a khan"},
    {"_id":1002,"Name":"Mobeen","Age":28,"City":"Mardan","Bio":"I am a fac"},
    {"_id":1003,"Name":"Ali","Age":29,"City":"Charsadda","Bio":"I am a wats"},
    {"_id":1004,"Name":"Shahriyar","Age":30,"City":"Swaat","Bio":"I am a youtuber"},
    {"_id":1005,"Name":"Muhammad","Age":32,"City":"Umerzai","Bio":"I am a you"},
    {"_id":1006,"Name":"Shahriyar","Age":20,"City":"Noshihra","Bio":"I am a twitter"},
    {"_id":1008,"Name":"Shahriyar","Age":20,"City":"Noshihra","Bio":"I am a youtuber",
     "experienc":[
         {"Company":"Amazon"},
         {"Company":"Google"}
     ]}
    
]
collection.insert_many(records)
print("Data inserted")