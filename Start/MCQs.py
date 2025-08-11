from Questions import Questions
question_promts = [
    "what color are apple?\n(a) Red\n(b) Yellow\n(c) Green\n",
    "What color is banana?\n(a) Red\n(b) Yellow\n(c) Green\n",
]

questions = [
    Questions(question_promts[0], "a"),
    Questions(question_promts[1], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score is "+str(score)+"/"+str(len(questions)))
run_test(questions)