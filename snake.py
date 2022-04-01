# snake class for snake project
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

#create initial snake body at initial position
class Snake:
    """Models each snake segment."""
    def __init__(self):
        self.segments = []                          # bundeling all parts of snake together. 
        self.create_snake()
        self.head = self.segments[0]                # DECLARING WHICH PART OF SNAKE IS THE HEAD
        self.tail = self.segments[-1]

    def create_snake(self): 
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def grow_snake(self):  # adds a new segment to the snake
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            self.segments.append(new_segment)
            
        

             
#get snake to automatically move forwards together
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # controls for the snake
    def right(self):                        
        if self.head.heading() != LEFT:         # this stops the snake going back on itself
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:      
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:    
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)

