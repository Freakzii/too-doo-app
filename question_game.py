import json

from pyexpat.errors import messages

with open("questions.json",'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("answer"))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct"
    else:
        result = "wrong"
    message = f"{index +1} - {result} - Your answer: {question['user_choice']},"\
                f"{index +1}- {result} - correct answer:{question['correct_answer']}"
    print(message)