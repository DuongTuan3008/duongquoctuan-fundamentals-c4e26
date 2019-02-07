from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
n=3
for o in range(len(colors)):
    for i in range(n):
        pencolor(colors[n-3])
        fd(100)
        lt(180-((n-2)*180)/n)
    n+=1
done()