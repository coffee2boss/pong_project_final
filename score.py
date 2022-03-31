from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.setposition(0, 280)
        self.speed("fastest")
        self.write(f"Score = {self.score}", align="center", font=("Arial",12,"normal"))

    def increase_score(self):
        self.score += 1
        self.write(f"Score = {self.score}", align="center", font=("Arial",12,"normal"))

  
    



    
        