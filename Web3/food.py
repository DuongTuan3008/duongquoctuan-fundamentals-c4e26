from db import food_collection


new_food_name = input("Enter name: ")
new_food_price = int(input("Enter price: "))
new_food = {
    "name": new_food_name,
    "price": new_food_price,
}
food_collection.insert_one(new_food)

# if __name__ == "__main__":
#     while True:
#         new_food_name = input("Enter name: ")
#         new_food_price = int(input("Enter price: "))

#         add_food(new_food_name, new_food_price)
food_list = food_collection.find(
    {
        "name": "Bun cha"
    }
)

for food in food_list:
    if food["name"] == "Bun cha":
        print(food["name"])
        print(food["price"])