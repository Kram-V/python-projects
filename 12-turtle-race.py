from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=500)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ['red', 'black', 'green', 'blue', 'orange', 'purple']
all_turtles = []

y = -100

if user_input not in colors:
    print("You have invalid input!")
else:
    for turtle_index in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-490, y=y)
        y += 40
        all_turtles.append(new_turtle)

    is_race_on = True
    winning_color = None

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 470:
                is_race_on = False
                winning_color = turtle.pencolor()
                break
            else:
                rand_distance = random.randint(1, 10)
                turtle.forward(rand_distance)

    if winning_color == user_input:
        print("You Won!")
    else:
        print("You Lose!")

    screen.bye()