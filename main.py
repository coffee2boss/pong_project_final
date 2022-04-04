import time
from turtle import Screen, color
from paddles import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_a = Paddle((-370,0))
paddle_b = Paddle((370,0))
ball = Ball()

#MOVEMENT FOR PADDLE A
screen.listen()
screen.onkey(paddle_a.go_up, "q")    #UP                  # input and ties to the controls for paddle_a
screen.onkey(paddle_a.go_down, "a")    #DOWN

#MOVEMENT FOR PADDLE B
screen.onkey(paddle_b.go_up, "p")    #UP                    # input and ties to the controls for paddle_b
screen.onkey(paddle_b.go_down, "l")    #DOWN


# Get snake to automatically move forwards
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)         # this can be adjusted to adjust the speed of the ball 
    screen.update()  
    ball.move()

    # detect if ball hits wall on y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect if ball hits paddles on x axis
    if ball.distance(paddle_a) < 40 and ball.xcor() < -350 :
        ball.paddle_bounce()
        
    elif ball.distance(paddle_b) < 40 and ball.xcor() > 350:
        ball.paddle_bounce()
    
    # detect if player scores
    if ball.xcor() == 380:
        scoreboard.clear()
        scoreboard.increase_score_A()
        scoreboard.update_scoreboard()
        ball.refresh()
        ball.move()
    
    if ball.xcor() == -380:
        scoreboard.clear()
        scoreboard.increase_score_B()
        scoreboard.update_scoreboard()
        ball.refresh()
        ball.paddle_bounce()

    #End of game
    if scoreboard.score_B == 10:
        game_is_on = False
        scoreboard.game_over()
    elif scoreboard.score_A == 10:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
