from data import question_data
from quiz_brain import QuizBrain

quiz = QuizBrain(question_data)
current_score = 0

is_questioning = True

while is_questioning:
  user_answer = quiz.current_question()

  if user_answer not in('True', 'False'):
    print("Your answer is invalid.")
    continue

  if user_answer == quiz.current_answer():
    print("You got it right! 🎉")

    current_score += 1
    print(f"Your current score is: {current_score}/{quiz.current_question_number()}\n\n")

    if not quiz.has_a_question():
      is_questioning = False
      print("🎉 You've completed the quiz!")
      print(f"Your final score was: {current_score}/{quiz.current_question_number()}")

      percentage = quiz.score / quiz.question_number * 100
      
      if percentage == 100:
          print("Perfect score! You're a web development pro! 🏆")
      elif percentage >= 70:
          print("Great job! You know your stuff.")
      elif percentage >= 40:
          print("Not bad! A little more practice and you'll nail it.")
      else:
          print("Keep learning, you'll do better next time!")
      exit()

    quiz.next_question()

    continue
  else:
    print("Sorry, that's incorrect.")
    print(f"The correct answer was: {quiz.current_answer()}")
    print(f"Your current score is: {current_score}/{quiz.current_question_number()}\n\n")
    
    if not quiz.has_a_question():
      is_questioning = False
      print("🎉 You've completed the quiz!")
      print(f"Your final score was: {current_score}/{quiz.current_question_number()}")

      percentage = current_score / (quiz.current_question_number()) * 100

      if percentage == 100:
          print("Perfect score! You're a web development pro! 🏆")
      elif percentage >= 70:
          print("Great job! You know your stuff.")
      elif percentage >= 40:
          print("Not bad! A little more practice and you'll nail it.")
      else:
          print("Keep learning, you'll do better next time!")
      exit()

    quiz.next_question()
    
    continue




