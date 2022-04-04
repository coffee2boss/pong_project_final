from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12 , "normal")
FONT2 = ("Courier", 20 , "bold")

class Scoreboard(Turtle):

    def __init__(self):
    
            super().__init__()
            self.color("white")
            self.hideturtle()
            self.penup()
            self.score_A = 0
            self.score_B = 0
            self.update_scoreboard()
            
            

    def update_scoreboard(self):
        self.goto(-60, 280)
        self.write(f"Score A = {self.score_A}", align=ALIGNMENT, font=FONT)
        self.goto(60, 280)
        self.write(f"Score B = {self.score_B}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT2)

    def increase_score_A(self):
        self.score_A += 1
        self.update_scoreboard()

    def increase_score_B(self):
        self.score_B += 1
        self.update_scoreboard()

  
    



    
        