# Write a function that prints out “Hello world” 3 times
def hello3():
    for i in range(3):
        print("Hello world")
#2.	Write a function that takes 2 numbers as arguments 
# and print out sum of them
def add_sum(x,y):
    print(x+y)
#3.	Write a Python function that draws a square, named draw_square, 
# takes 2 arguments: length and color, 
# where length is the length of its side and 
# color is the color of its bound (line color)
def square_draw(length,colors):
    import turtle as t
    t.shape("turtle")
    t.speed(5)
    t.color(colors)
    for i in range (4):
        t.pendown()
        t.forward (length)
        t.left(90)
# square_draw(200,"red")

#4.	another programmer named ‘T.Anh’ will use your code in exercise 
from turtle import *
for i in range(30):
    square_draw(i * 50, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#5. Draw a star
def draw_star(x,y,length):
    import turtle as t
    t.shape("turtle")
    t.setpos(0,0)
    t.speed(5)
    for i in range(5):
        t.right(144)
        t.forward(length)
# draw_star(90,100,200)

#6. Debug draw a star
from turtle import *
speed(0)
color('blue')
for i in range(10):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 100)
    draw_star(x, y, length)


