from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake.make_segments()

food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.stop_game, "Escape")


while snake.is_gaming:
  screen.update()
  time.sleep(0.1)

  snake.move()

  if snake.segments[0].distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    snake.add_segment()

  if snake.segments[0].xcor() > 380 or snake.segments[0].xcor() < -380 or snake.segments[0].ycor() > 380 or snake.segments[0].ycor() < -380:
    scoreboard.get_high_score()
    snake.new_game()
    continue

  for segment in snake.segments:
    if segment == snake.segments[0]:
      pass
    elif snake.segments[0].distance(segment) < 10:
      scoreboard.get_high_score()
      snake.new_game()


  
