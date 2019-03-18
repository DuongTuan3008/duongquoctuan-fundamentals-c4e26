from db import food_collection
from bson import ObjectId
def add_food(name, price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)

def get(query): # filter, limit = 5, skip = 10
    food_list = food_collection.find(query)
    return food_list

# if __name__ == "__main__":    
#     food_list = food_collection.find(
#         {
#             "price": { "$gte":25000 },
#         } # query
#     ) # 

def get_by_id(id):
    f = food_collection.find_one({ "_id":ObjectId(id) })
    return f

def delete_by_id(id):
    food_collection.delete_one({"_id":ObjectId(id)})

def update_by_id(id, name, price):
    query = {"_id": ObjectId(id)}
    updater = {
        "$set": { "price": price },
        "$set": { "name" : name },
        # $inc, $dec, $set, $unset
    }
    food_collection.find_one_and_update(query, updater)

# if __name__ == "__main__":
    # delete_by_id("5c85f3cbaf1137320c9d3871")
    # f = get_by_id("5c85f37caf11372998fd5c3a")
    # # for food in get({"_id":ObjectId("5c85f37caf11372998fd5c3a")}):
    # if f !=None:
    #     print(f["name"])
    # add_food("Nem Cua Bể", 15000)
    # add_food("Cháo Lòng", 30000)
    # add_food("Bún Riêu Cua", 25000)
    # query = {"_id": ObjectId("5c8a5c9caf11373be84d6da1")}
    # updater = {"$set": { "price": 40000 } } # $inc, $dec, $set, $unset
    # # food_collection.find_one_and_update(query, updater)
    # print(*get({}), sep="\n")