class QuizBrain:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list

  def next_question(self):
    self.question_number += 1

  def current_question(self):
    question = self.question_list[self.question_number].question
    
    return input(f"Question #{self.question_number + 1}: {question} (true or false)? ").capitalize()

  def current_answer(self):
      return self.question_list[self.question_number].answer

  def current_question_number(self):
    return self.question_number + 1

  def has_a_question(self):
    if self.question_number == len(self.question_list) - 1:
      return False
    else:
      return True