import time, turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def reset_game():
    snake.reset()
    scoreboard.reset()


# snake game setup
T_INTERVAL = .1

# screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# place snake, food, and scoreboard on screen
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# listeners
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# driver to move snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(T_INTERVAL)  # adds a T_INTERVAL delay after each segment moves
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        reset_game()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # for each segment, check if the head is less than 10 paces away (
            # collision)
            reset_game()

screen.mainloop()
