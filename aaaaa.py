from turtle import *
t = Turtle()
t.color("blue")
t.shape("circle")
t.width(5)
t.pendown()
t.speed(100)
def draw(x,y):
    t.goto(x,y)

t.ondrag(draw)


def c_red():
    t.color("red")

def c_green():
    t.color("green")

def c_yellow():
    t.color("yellow")





def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()



def up():
    t.goto(t.xcor(),t.ycor()+15)
def down():
    t.goto(t.xcor(),t.ycor()-15)
def left():
    t.goto(t.xcor()-15,ycor())
def right():
    t.goto(t.xcor()+15,ycor())

def bf():
    t.begin_fill()
def ef():
    t.end_fill()

scr = t.getscreen()


scr.onkey(c_red,'2')
scr.onkey(c_green,'3')
scr.onkey(c_yellow,'4')
scr.onkey(up,'w')
scr.onkey(down,'s')
scr.onkey(left,'a')
scr.onkey(right,'d')
scr.onkey(bf,'z')
scr.onkey(ef,'x')


scr.onscreenclick(move)

scr.listen()