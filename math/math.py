import math
import json
import random

"""
Program to generate math quizzes quickly and easily.
"""

class QuizQuestion:
    def __init__(self, question, correct_answer, wrong_answers, timeout=15):
        self.question = question
        self.correctAnswer = correct_answer
        self.wrongAnswers = wrong_answers
        self.timeout = timeout
        
def generate_math_question():
    smallNum1 = random.randint(2, 6)
    smallNum2 = random.randint(2, 6)
    num1 = random.randint(2, 100)
    num2 = random.randint(2, 100)
    operation = random.choice(['+', '-', '*', '/', '!' , '^','root'])
    
    if operation == '+':
        question = f"What is {num1} + {num2}?"
        correct_answer = num1 + num2
    elif operation == '-':
        question = f"What is {num1} - {num2}?"
        correct_answer = num1 - num2
    elif operation == '*':
        question = f"What is {num1} * {num2}?"
        correct_answer = num1 * num2
    elif operation == '/':
        num1 = num1 * num2
        question = f"What is {num1} / {num2}?"
        correct_answer = num1 // num2
    elif operation == '!':
        question = f"What is {smallNum1}!?"
        correct_answer = math.factorial(smallNum1)
    elif operation == '^':
        question = f"What is {smallNum1}^{smallNum2}?"
        correct_answer = smallNum1**smallNum2
    elif operation == 'root':
        question = f"What is the square root of {(smallNum1*2)*(smallNum1*2)}?"
        correct_answer = smallNum1 * 2
    
    wrong_answers = set()
    # For loop does not work as some answers may be equal to the correct answer or another wrong answer
    while len(wrong_answers) < 3:
        wrong_answer = correct_answer + random.randint(-10, 10)
        if wrong_answer != correct_answer and wrong_answer not in wrong_answers:
            wrong_answers.add(wrong_answer)
    
    return QuizQuestion(question, str(correct_answer), list(wrong_answers))

def generate_quiz(num_questions):
    questions = []
    seen_questions = set()
    attempts = 0
    max_attempts = num_questions * 10
    while len(questions) < num_questions and attempts < max_attempts:
        question_obj = generate_math_question()
        if question_obj.question not in seen_questions:
            questions.append(question_obj)
            seen_questions.add(question_obj.question)
        attempts += 1
    if len(questions) < num_questions:
        print(f"Warning: Only generated {len(questions)} unique questions out of {num_questions} requested.")
    return questions

def save_quiz_to_json(questions, file_path, title):
    quiz_data = {
        "title": title,
        "listOfQuestions": [vars(q) for q in questions],
        "time given": 15
    }
    with open(file_path, 'w') as file:
        json.dump(quiz_data, file, indent=4)

def returnQuiz(numOfQuestions):
    questions = generate_quiz(numOfQuestions)
    return "Math Quiz", questions

if __name__ == '__main__':
    title = input("Title:")
    num_questions = int(input("Number of Questions"))
    questions = generate_quiz(num_questions)
    filepath = f'{title}.json'
    save_quiz_to_json(questions, filepath, title)
    print(f"Generated a {num_questions}-question math quiz and saved to {filepath}")