from pymongo import MongoClient

uri = "mongodb+srv://tuandeptrai:icanfly9@cluster0-eb69h.mongodb.net/test?retryWrites=true"

# 1. Connect
client = MongoClient(uri)

# 2. Get Database
db = client.test 

# 3. Get Collection
food_collection = db["food"]
user_collection = db["users"]

# # 4. Create a new document
# new_food = {
#     "name": "Bun cha",
#     "price": 30000,
# } # document

# # 5. Insert new document into collection
# food_collection.insert_one(new_food)

# 6. Close connection
def close():
    client.close()

