from random import *
from is_inside import *
shapes = [
    {
        'text': 'BLUE',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'RED',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'YELLOW',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'GREEN',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    color = choice(['BLUE','RED','YELLOW','GREEN',])
    meaning = choice(['#3F51B5','#C62828','#FFD600','#4CAF50',])
    return [
                color,
                meaning,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    # if quiz_type == 0:
    print("Check inside")
    for shape in shapes:
        if is_inside([x,y],shape['rect']):
            if quiz_type == 0 and shape['text'] == text:
                return True
            elif quiz_type == 1 and shape['color'] == color:
                return True
            else: 
                return False
        
    
