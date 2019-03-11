from turtle import  * 


shape("turtle")
n = 4 
speed(15)
color('red')
left(30)
for i in range (n):
   forward(100)
   right(60)
   forward(100) 
   right(120)
   forward(100)
   right(60)
   forward(100)
   left(150)
mainloop()