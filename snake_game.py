from turtle import Turtle, Screen, position
import time
from typing import Set
screen = Screen()
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)
all_turtle = []
start_pos = [(0,0),(-20,0),(-40,0)]
for pos in start_pos:
    turts = Turtle()
    turts.shape("square")
    turts.penup()
    turts.speed("slowest")
    turts.goto(pos)
    all_turtle.append(turts)
def when_up():
    all_turtle[0].setheading(90)
def when_down():
    all_turtle[0].setheading(270)
def when_left():
    all_turtle[0].setheading(180)
def when_right():
    all_turtle[0].setheading(0)
game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    for j in range(len(all_turtle)-1,0,-1):
        pos =(all_turtle[j-1].xcor(), all_turtle[j-1].ycor())
        all_turtle[j].goto(pos)
        

    all_turtle[0].forward(20)
    
    if all_turtle[0].xcor() == 300 or all_turtle[0].xcor() == -300 or all_turtle[0].xcor() > 300 or all_turtle[0].xcor() < -300 or all_turtle[0].ycor() == 300 or all_turtle[0].ycor() == -300 or all_turtle[0].ycor() > 300 or all_turtle[0].ycor() < -300:
        game_on = False
        print ("game over")
    screen.listen()
    screen.onkey(key ="w", fun=(when_up))
    screen.onkey(key ="a", fun=(when_left))
    screen.onkey(key ="s", fun=(when_down))
    screen.onkey(key ="d", fun=(when_right))
    


    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
















screen.exitonclick()