client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-oskz4.mongodb.net/test?retryWrites=true&w=majority")
mydb = client['mydatabase']
mycol = mydb["students"]
#create db
mydb = myclient["mydatabase"]
dblist = myclient.list_database_names()

#create collection
mycol = mydb["customers"]
print(mydb.list_collection_names())

#insert into collection 
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#Return id
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

#Inser multiple documents
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

#Insert Multiple Documents, with Specified IDs
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

#find one
x = mycol.find_one()
print(x)

#find all
for x in mycol.find():
  print(x)

#Return Only Some Fields
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

#Filter the Result
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

#Advanced Query
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

#Filter With Regular Expressions
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

#Sort the Result
mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x)

#Sort Descending
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)

#delete document
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

#Delete Many Documents
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)

#Delete All Documents in a Collection
x = mycol.delete_many({})

#Drop collection
mycol.drop()

#update one
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)

#update many
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)

#limit the result
myresult = mycol.find().limit(5)

