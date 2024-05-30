## Code by Samir Talukder 
# All Credits are reserved 

import random

class PythonStudyPartner:
    def __init__(self):
        self.topics = {
            'variables': self.variables_quiz,
            'data_types': self.data_types_quiz,
            'loops': self.loops_quiz,
            'functions': self.functions_quiz
        }
        self.progress = {topic: 0 for topic in self.topics}

    def variables_quiz(self):
        questions = [
            ("What is a variable in Python?", "A variable is a container for storing data values."),
            ("How do you assign a value to a variable?", "Using the equal sign (=). Example: x = 5"),
            ("Can variable names start with a number?", "No, variable names must start with a letter or the underscore character.")
        ]
        return self.ask_questions(questions)

    def data_types_quiz(self):
        questions = [
            ("Name three common data types in Python.", "int, float, str"),
            ("What is the data type of 3.14?", "float"),
            ("What is the data type of 'Hello, World!'?", "str")
        ]
        return self.ask_questions(questions)

    def loops_quiz(self):
        questions = [
            ("What is a loop in Python?", "A loop is used to iterate over a sequence (such as a list, tuple, or string)."),
            ("What is the syntax for a 'for' loop?", "for variable in sequence:"),
            ("What is the syntax for a 'while' loop?", "while condition:")
        ]
        return self.ask_questions(questions)

    def functions_quiz(self):
        questions = [
            ("What is a function in Python?", "A function is a block of code which only runs when it is called."),
            ("How do you define a function in Python?", "Using the def keyword. Example: def my_function():"),
            ("Can a function return a value?", "Yes, using the return statement.")
        ]
        return self.ask_questions(questions)

    def ask_questions(self, questions):
        score = 0
        for question, correct_answer in questions:
            print(question)
            answer = input("Your answer: ")
            if answer.strip().lower() == correct_answer.strip().lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}\n")
        return score

    def show_progress(self):
        for topic, score in self.progress.items():
            print(f"{topic}: {score} correct answers")

    def study(self):
        while True:
            print("\nChoose a topic to study:")
            for topic in self.topics:
                print(f"- {topic}")
            print("- exit")
            choice = input("Your choice: ").strip().lower()
            if choice == 'exit':
                print("Goodbye! Keep studying and practicing!")
                break
            elif choice in self.topics:
                print(f"Starting quiz on {choice}...\n")
                score = self.topics[choice]()
                self.progress[choice] += score
                print(f"Your score for {choice}: {score}\n")
                self.show_progress()
            else:
                print("Invalid choice. Please try again.")

# Instantiate the study partner and start studying
study_partner = PythonStudyPartner()
study_partner.study()
