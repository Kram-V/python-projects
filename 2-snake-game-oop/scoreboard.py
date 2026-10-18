from turtle import Turtle
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, 'high-score-persists.txt')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open(DATA_FILE) as data:
      self.high_score = int(data.read())
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(-100, 360)
    self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    self.goto(100, 360)
    self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

  def increase_score(self):
    self.score += 1
    self.clear()
    self.goto(-100, 360)
    self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    self.goto(100, 360)
    self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

  def get_high_score(self):
    if self.score > self.high_score:
      self.high_score = self.score

      with open(DATA_FILE, mode='w') as file:
        file.write(str(self.high_score))

      self.score = 0
      self.clear()
      self.goto(-100, 360)
      self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
      self.goto(100, 360)
      self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    else:
      self.score = 0
      self.clear()
      self.goto(-100, 360)
      self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
      self.goto(100, 360)
      self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
