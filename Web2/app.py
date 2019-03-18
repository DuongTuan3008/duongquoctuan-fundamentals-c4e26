from flask import Flask, render_template, request
app = Flask(__name__)

items = [
    {
        "name": "Com rang",
        "price": 25000,
    },
    {
        "name": "Pho bo",
        "price": 30000,
    },
    {
        "name": "Xoi xeo",
        "price": 10000,
    }
]

users = "Tuan"

@app.route("/")
def menu():
    return render_template("menu.html", item_list=items, user=users)

@app.route("/food/<int:i>")
def food(i):
    f = items[i]
    return render_template("food_detail.html", item=f)

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        price = form["price"]
        new_item = {
            "name": name,
            "price": price,
        }
        items.append(new_item)
        return name + " added"

if __name__ =="__main__":
    app.run(debug=True)