from turtle import Turtle

class Snake:
  def __init__(self):
    self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    self.segments = []

  def make_segments(self):
    for coords in self.starting_positions:
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(coords)
      self.segments.append(new_segment)

  def add_segment(self):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()

    new_segment.goto(self.segments[-1].position())
    self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1): # start, stop and step
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
      
    self.segments[0].forward(20)

  def up(self):
      if self.segments[0].heading() != 270:
          self.segments[0].setheading(90)

  def down(self):
      if self.segments[0].heading() != 90:
          self.segments[0].setheading(270)

  def left(self):
      if self.segments[0].heading() != 0:
          self.segments[0].setheading(180)

  def right(self):
      if self.segments[0].heading() != 180:
          self.segments[0].setheading(0)


