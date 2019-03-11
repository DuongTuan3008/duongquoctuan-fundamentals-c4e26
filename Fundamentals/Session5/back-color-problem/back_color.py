from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes
def is_inside(x=[0,0],y=[0,0,0,0]):
    if (len(x)==2 and len(y)==4) == False:
        return False
    else:
        x_axis = (x[0]>y[0]) and (x[0]<y[0]+y[2])
        y_axis = (x[1]>y[1]) and (x[1]<y[1]+y[3])
        if (x_axis and y_axis) == False:
            return False
        else:
            return True
def generate_quiz():
    index_1 = randint(0,3)
    index_2 = randint(0,3)
    text = shapes[index_1]["text"]
    color = shapes[index_2]["color"]
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]
def find_index(dicts, key, value):
    class Null: pass
    for i, d in enumerate(dicts):
        if d.get(key, Null) == value:
            return i
    else:
        raise ValueError('no dict with the key and value combination found')
def mouse_press(x, y, text, color, quiz_type):
    a = [x,y]
    if quiz_type == 0:
        index = find_index(shapes,"text",text) 
        rect = shapes[index]["rect"]
    else:
        index = find_index(shapes,"color",color) 
        rect = shapes[index]["rect"]
    return is_inside(a,rect)
