#Learning how to make MCQ game in python using classes, loops and if conditions

from ques import question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Yellow\n(c) Black\n\n",
    "What color are Bananas?\n(a) Red\n(b) Yellow\n(c) Black\n\n",
    "What color are Strawberries?\n(a) Red\n(b) Yellow\n(c) Black\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+= 1
    print("You got " +str(score) +" question(s) right!" )

run_test(questions)