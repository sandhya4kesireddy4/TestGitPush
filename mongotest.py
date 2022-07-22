import pymongo
client = pymongo.MongoClient("mongodb+srv://sandhyakesireddy1:Password01@cluster0.w3ubldt.mongodb.net/?retryWrites=true&w=majority")
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "sandhya",
    "email":"sandhya.kesireddy@gmail.com",
    "lastname": "kesireddy"
}
d1={
    "name": "Nisha",
    "email":"nisha.purumandla@gmail.com",
    "lastname": "purumandla"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)