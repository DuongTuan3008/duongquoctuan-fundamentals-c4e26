from flask import Flask, redirect
app = Flask(__name__)
# Bind route to view function
@app.route("/") # route
def home(): # view function
    return "C4E, Hello"

@app.route("/myclass")
def myclass():
    return "C4E26, Son, Tuan, ..."

@app.route("/hi/<name>")
def hi_duc(name):
    return "Hi, " + name

@app.route("/add/<int:n>/<int:n1>")
def add(n,n1):
    s = n + n1
    return str(s)

items = ["Com", "Pho", "Bun Cha"]
@app.route("/menu")
def menu(): 
    return str(items)

@app.route("/food/<int:i>")
def food(i):
    return items[i]

@app.route("/about-me")
def info():
    info = {"Name": "Tuấn","Work": "Jobless","School" :"Hanu","Hobbies" :"Sleeping"}
    return str(info)

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
