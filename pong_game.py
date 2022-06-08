
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.tracer(0)

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(pos, 0)
        
    def when_up(self):
        if (self.ycor() + 20) < 260:
            newy = int(self.ycor() + 20)
            self.goto(self.xcor(),newy)
            # print(self.xcor(), self.ycor())

    def when_down(self):
        if (self.ycor() + 20) > -220:
            newy = int(self.ycor() - 20)
            self.goto(self.xcor(),newy)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_cor = 10
        self.y_cor = 10
    
    def start(self):
        self.goto(self.xcor() + self.x_cor, self.ycor() + self.y_cor)
        # print("{} and {}".format(self.xcor() + self.addd, self.ycor() + self.addd))
    
    def bounce_x(self):
        self.y_cor *= -1  
    
    def bounce_y(self):
        self.x_cor *= -1
        
    def miss(self):
        self.goto(0,0)
        
class Scoreboard(Turtle):
    def __init__(self, x2):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.x2 = x2
        
        
    def score(self, score):
        self.clear()
        self.goto(self.x2, 240)
        self.write(score, font=("arial", 20, "normal"))
        
def winlose(x,y,z):
    winlose = Turtle()
    winlose.shape("circle")
    winlose.hideturtle()
    winlose.color("black")
    winlose.penup()
    winlose.goto(x,y)
    winlose.write("{}".format(z), font=("arial", 20, "normal"))
    
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
sboard1 = Scoreboard(20)
sboard2 = Scoreboard(-20)

screen.listen()
screen.onkeypress(key ="w", fun = left_paddle.when_up)
screen.onkeypress(key ="s", fun = left_paddle.when_down)
screen.onkeypress(key ="Up", fun = right_paddle.when_up)
screen.onkeypress(key ="Down", fun = right_paddle.when_down)
game_on = True
sboard1.score(0)
sboard2.score(0)
while game_on:
    time.sleep(0.05)
    screen.update()
    
    ball.start()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_x()
    # print ("{} and {} and {}".format(ball.xcor(), right_paddle.ycor(), ball.ycor()))
    if ball.xcor()==340 and (right_paddle.ycor()==ball.ycor() or right_paddle.ycor() + 20 == ball.ycor() or right_paddle.ycor() + 40 == ball.ycor() or right_paddle.ycor() - 20 == ball.ycor() or right_paddle.ycor() -40 == ball.ycor()):
        ball.bounce_y()
        sboard1.score2 += 1
    elif ball.xcor()>380:
        ball.miss()
        if sboard1.score2 == 0:
            winlose(40,200,"you lose")
            game_on = False
        elif sboard1.score2 == 1 or sboard1.score2>1:
            sboard1.score2 -= 1
    
    sboard1.score(sboard1.score2)
        
    if ball.xcor()==-340 and (left_paddle.ycor()==ball.ycor() or left_paddle.ycor() + 20 == ball.ycor() or left_paddle.ycor() + 40 == ball.ycor() or left_paddle.ycor() - 20 == ball.ycor() or left_paddle.ycor() -40 == ball.ycor()):
        ball.bounce_y()
        sboard2.score1 += 1
        
    elif ball.xcor()<-380:
        ball.miss()
        if sboard2.score1 == 0:
            winlose(-120,200,"you lose")
            game_on = False
        elif sboard2.score1 == 1 or sboard2.score1>1:
            sboard2.score1 -= 1
    sboard2.score(sboard2.score1)
    
    if sboard1.score2 > 3 or sboard2.score1 > 3:
        if sboard1.score2 - sboard2.score1 == 3:
            winlose(40,160,"Winner")
            game_on = False
        if sboard2.score1 - sboard1.score2 == 3:
            winlose(-120,160,"Winner")
            game_on = False
            
screen.exitonclick()