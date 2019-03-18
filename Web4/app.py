from flask import Flask, render_template, request, redirect, url_for
from db import db
import food
app = Flask(__name__)

food_collection = db["food"]

@app.route("/")
def welcome():
    return redirect(url_for("food_list"))

@app.route("/food_list")
def food_list():
    all_food = food.get({})
    return render_template("food_list.html", f_list=all_food,)

@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return render_template("food_detail.html", f = f)

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        price = form["price"]
        food.add_food(name, price)
        return name + " added"

@app.route("/user/add", methods=["GET","POST"])
def add_user():
    if request.method=="GET":
        return render_template("add_user.html")
    elif request.method=="POST":
        form=request.form
        u=form["username"]
        p=form["password"]
        new_user={
            "username":u,
            "password":p
        }
        user_collection.insert_one(new_user)
        return "New user added"

@app.route("/user", methods=["GET","POST"])
def user():
    if request.method=="GET":
        return render_template("user.html")
    elif request.method=="POST":
        form=request.form
        us=form["username"]
        pas=form["password"] 
        user={
            "username":us,
            "password":pas
        }
        a = user_collection.find_one(user["username"])
        if a ==None:
            return "This user doesn't exist. Please register a new account."

if __name__ =="__main__":
    app.run(debug=True)