from flask import Flask, redirect
app = Flask(__name__)

@app.route("/bmi/<w>/<h>")
def BMI(w,h):
    BMI_calc = int(w)/(int(h)**2)
    if BMI_calc < 16:
      bmi = "Severely underweight"
    elif BMI_calc < 18.5:
      bmi = "Underweight"
    elif BMI_calc < 25:
      bmi = "Normal"
    elif BMI_calc < 30:
      bmi = "Overweight"
    else:
      bmi = "Obese"
    return bmi


@app.route("/user/<name>")
def username(name):
  Users = { "huy":{"name":"Nguyen Quang Huy", 
                          "location":"Hanoi", 
                          "Job":"Teacher"},
                "duc":{"name":"Hoang Huy Duc",
                          "location":"HaiPhong",
                          "Job":"T.A"},
                "tuan":{"name":"Duong Quoc Tuan",
                          "location":"Hanoi",
                          "Job":"Student"}
                }
  if name in Users:
    return str(Users[name])
  else:
    return "User not found"



if __name__ == '__main__':
  app.run(debug=True)