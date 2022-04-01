import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")                        # input and ties to the controls for the snake
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#get snake to automatically move forwards
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect snake head with food
    if snake.head.distance(food) < 15:
        print("nom nom nom!!")
        snake.grow_snake()
        food.refresh()
        scoreboard.increase_score()

    # SNAKE HITS WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        print("Game over!!")
        scoreboard.game_over()
        
    


screen.exitonclick()
