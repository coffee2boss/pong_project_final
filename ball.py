from turtle import Turtle, xcor

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.penup()
        self.color("blue")
        self.ball_speed = 0.09
        self.refresh()
        self.x_move = 5
        self.y_move = 10


    def refresh(self):    
        self.goto(0,0)
        self.ball_speed = 0.09

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        #self.forward(20)        # this distance in the bracket is being used to adjust the speed of the ball. higher num = higher speed