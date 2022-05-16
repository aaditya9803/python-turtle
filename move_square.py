from turtle import Turtle, Screen
my_turtle = Turtle()
def forward():
    my_turtle.forward(100)
def left():
    my_turtle.left(90)
def right():
    my_turtle.right(90)
def backward():
    my_turtle.back(100)
def clearscreen():
    my_turtle.clear()
    my_turtle.home()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.speed("fastest")
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clearscreen)




screen.exitonclick()