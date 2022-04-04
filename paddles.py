# snake class for snake project
from turtle import Turtle
POSITION_LINE = (0,280)
POSITIONS = [(-370,0), (370,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

#create initial snake body at initial position
class Paddle(Turtle):
    """Models each paddle."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4 ,stretch_len=1, outline=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.go_up()
        self.go_down()
      

    
        

    def mid_line(self):
        for new_line in range(2):
            new_line = Turtle
            new_line.color("white")
            new_line.goto(POSITION_LINE)
            new_line.setheading(DOWN)
            new_line.penup()
            new_line.forward(10)
            new_line.pendown()
            new_line.forward(10)

    # controls for the paddle A
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    

 
