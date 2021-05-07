
"""
06/05/2021
Alvaro Garcia
Santiago Noriega A01023652
v.2


Paint, for drawing shapes.
Rectangle, circle, triangle and color(gray) funcionalities were added to this code. 

"""
import turtle                           #Import Libraries
from turtle import *
from freegames import vector

def line(start, end):                   #Function for a line
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):                 #Function for a square with fill
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):                     #Function for a circle with fill
   
    r = (end.x - start.x)/2
    up()
    goto(start.x + r, start.y)
    begin_fill()
    turtle.circle(r)
    end_fill()
    

def rectangle(start, end):               #Function for a rectangle with fill   
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x - start.x) 
        left(90)
        forward((end.x- start.x)/2)
        left(90)
    end_fill()

def triangle(start, end):               #Function for a triange with fill
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()

def tap(x, y):
                                "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
                                     "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')      #colors
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('gray'), 'X')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
