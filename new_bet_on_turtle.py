from pickle import TRUE
from turtle import Turtle, Screen
import random
screen = Screen()
choosen = screen.textinput(title="place your bet", prompt = "bet on red / green / blue / purple")
all_turtles = []
colors = ["red", "green", "blue", "purple"]
j = 60
    
for i in range(4):
    turt = Turtle()
    turt.color(colors[i])
    turt.shape("turtle")
    turt.goto(x=-230, y=j )
    turt.clear()
    all_turtles.append(turt)
    j -= 40
race_finished = False
while not race_finished:
    for turts in all_turtles:
        if turts.xcor() > 230:
            winner = turts.color()[1]
            race_finished = True
        else:
            turts.forward(random.randint(1,10))
        

inturt = Turtle()
inturt.color('black')
style = ('Arial', 35, 'italic')
style2 = ('Arial', 10, 'italic')

if choosen == winner:
    inturt.write('you win!', font=style, align='center')
else:
    inturt.write('you lose!', font=style, align='center')
    
inturt.write("{} wins the race".format(winner), font=style2, align='center')

inturt.hideturtle()
    
screen.exitonclick()
    