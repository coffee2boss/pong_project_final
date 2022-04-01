from ctypes import alignment
from turtle import Turtle, update
ALIGNMENT = "center"
FONT = ("Courier", 12 , "normal")
FONT2 = ("Courier", 20 , "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.setposition(0, 280)
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT2)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

  
    



    
        