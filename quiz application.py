class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            user_answer = input(question.prompt + " ")
            if user_answer.lower() == question.answer.lower():
                self.score += 1
        self.display_score()

    def display_score(self):
        print("You got", self.score, "out of", len(self.questions), "questions correct.")


# Define your quiz questions
question1 = Question("What is the capital of France? ", "Paris")
question2 = Question("What is 2 + 2? ", "4")
question3 = Question("Which planet is known as the Red Planet? ", "Mars")

# Create a list of questions
questions = [question1, question2, question3]

# Create the quiz and run it
quiz = Quiz(questions)
quiz.run()
