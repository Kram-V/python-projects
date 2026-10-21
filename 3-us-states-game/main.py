from turtle import Screen, Turtle
import pandas

image = '3-us-states-game/blank_states_img.gif'

data = pandas.read_csv("3-us-states-game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

screen = Screen()
turtle = Turtle()

screen.title("U.S. States Game")
screen.addshape(image)
screen.setup(width=725, height=491)

turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

is_playing = True
score = 0

while is_playing:
  answer = screen.textinput(
      title=f"Guess the state ({score}/50)",
      prompt="What's another state's name?"
  )

  if answer is None:
    is_playing = False
  else:
    user_answer = answer.title()

    if user_answer in all_states and user_answer not in guessed_states:
      guessed_states.append(user_answer)
      score += 1
      state = data[data.state == user_answer]
      writer.goto(state.x.item(), state.y.item())
      writer.write(user_answer, align="center", font=("Arial", 8, "normal"))