from turtle import Turtle, Screen
import time
import random
random_turt = Turtle()
random_turt.shape("circle")
random_turt.color("red")
pos_for_food = []
for _ in range(-260, 280, 20):
    pos_for_food.append(_)

screen = Screen()
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)
all_turtle = []
start_pos = [(0,0),(-20,0),(-40,0)]
def create_turtles():
    turts = Turtle()
    turts.shape("square")
    turts.penup()
    turts.speed("slowest")
    turts.goto(pos)
    all_turtle.append(turts)
    
for pos in start_pos:
    create_turtles()
    
def when_up():
    all_turtle[0].setheading(90)
def when_down():
    all_turtle[0].setheading(270)
def when_left():
    all_turtle[0].setheading(180)
def when_right():
    all_turtle[0].setheading(0)

def create_pos():
    x_po = random.choice(pos_for_food)
    y_po = random.choice(pos_for_food)
    return (int(x_po), int(y_po))

def form_food():
    
    random_turt.penup()
    food_pos = create_pos()
    random_turt.goto(food_pos)
    
food_found = False
first_food = True
game_on = True

# if first_food == True:
#     form_food()
    
# form_food(int(random.choice(pos_for_food)),int(random.choice(pos_for_food)))
all_turtle[0].color("green")
while game_on == True:
    screen.update()
    time.sleep(0.1)
    for j in range(len(all_turtle)-1,0,-1):
        pos =(all_turtle[j-1].xcor(), all_turtle[j-1].ycor())
        all_turtle[j].goto(pos)
    all_turtle[0].forward(20)
    
    
    screen.listen()
    screen.onkey(key ="w", fun=(when_up))
    screen.onkey(key ="a", fun=(when_left))
    screen.onkey(key ="s", fun=(when_down))
    screen.onkey(key ="d", fun=(when_right))
    random_pos = (int(round(random_turt.xcor())), int(round(random_turt.ycor())))
    po_head = (int(round(all_turtle[0].xcor())), int(round(all_turtle[0].ycor())))
    if po_head == random_pos:
        print ("reached")
        create_turtles()
        form_food()
    if all_turtle[0].xcor() == 300 or all_turtle[0].xcor() == -300 or all_turtle[0].xcor() > 300 or all_turtle[0].xcor() < -300 or all_turtle[0].ycor() == 300 or all_turtle[0].ycor() == -300 or all_turtle[0].ycor() > 300 or all_turtle[0].ycor() < -300:
        game_on = False
        print ("game over")
screen.exitonclick()