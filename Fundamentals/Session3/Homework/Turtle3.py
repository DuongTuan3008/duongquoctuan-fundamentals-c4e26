from turtle import  * 
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

shape("turtle")
speed(1)
left(180)
for n in range (3,8):
    print(n)
    color (colors[n-3])
    count_loops = 0
    while True:
        count_loops = count_loops + 1
        print(count_loops)
        right(180*2/n)
        forward (100)
        if count_loops >= n:
            break



mainloop()