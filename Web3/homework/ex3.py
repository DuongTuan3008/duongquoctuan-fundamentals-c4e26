import matplotlib.pyplot as plt 
from ex1 import db
customer_collection=db["customers"]
customers=customer_collection.find()
events=0
wom = 0
ads = 0
for c in customers:
    if c["ref"]=="events":
        events += 1
    elif c["ref"]=="wom":
        wom += 1
    else:
        ads += 1
slices = [events, wom, ads]
labels=["events","wom","ads"]
colors=["red","blue","yellow"]
plt.pie(slices, labels=labels, colors=colors)
plt.axis("equal")
plt.show() 

