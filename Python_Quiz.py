quiz = {
    1 : {
        "question" : "\nWho is the author of the general-purpose programming language Python, which he started working on in 1989, and is now among the most popular languages in use?",
        "answer" : "Guido van Rossum"
    },
    2 : {
        "question" : "\nIt is a loop inside the body of the outer loop.",
        "answer" : "Nested loop"
    },
    3 : {
        "question" : "\nIt is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.",
        "answer" : "Python"
    },
    4 : {
        "question" : "\nIt is an operation in Python that divides two numbers and rounds the result down to the nearest integer.",
        "answer" : "Floor division"
    },
    5 : {
        "question" : "\nIt is a function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.",
        "answer" : "Range"
    },
    6 : {
        "question" : "\nIt is the statement used to execute both the true part and the false part of a given condition.",
        "answer" : "if-else statement"
    }
}



def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"\nCorrect Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"\nWrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print("Welcome to the Python quiz! Are you ready to test your knowledge about Python?\n")
    print("There are a total of 6 questions, you can skip a question anytime by typing 'skip'\n")
    input("Press any key to start the quiz!")
    return True


# loops for question, attempts, skips, scores
intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

print(f"\nYour final score is {score}!\n\n")
print("Below are the correct answers! \n")
print_dictionary()
print("Thanks for playing!")
