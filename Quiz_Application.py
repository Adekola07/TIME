import random
#Question to be asked
quiz_data = [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyperlink Text Markup Language", "B. Hyper Transfer Markup Language", "C. Hypertext Markup Language", "D. High-Level Text Markup Language"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. JavaScript"],
        "answer": "D"
    },
    {
        "question": "What is the primary function of CSS in web development?",
        "options": ["A. Data storage", "B. Styling and layout", "C. Server-side scripting", "D. Database management"],
        "answer": "B"
    },
    {
        "question": "What does the acronym SQL stand for?",
        "options": ["A. Structured Query Language", "B. Simple Query Language", "C. Standard Query Language", "D. Sequential Query Language"],
        "answer": "A"
    },
    {
        "question": "Which programming language is often used for data analysis and scientific computing?",
        "options": ["A. JavaScript", "B. Java", "C. Python", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does API stand for in the context of web development?",
        "options": ["A. Application Programming Interface", "B. Advanced Programming Interface", "C. Automated Program Interaction", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of the following code: `print(3 * 'Hello ')`?",
        "options": ["A. Hello Hello Hello Hello", "B. 9", "C. Hello Hello Hello", "D. Syntax Error"],
        "answer": "C"
    },
    {
        "question": "In JavaScript, how do you declare a variable?",
        "options": ["A. var", "B. variable", "C. let", "D. declare"],
        "answer": "A"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of version control systems like Git?",
        "options": ["A. To write code", "B. To run code", "C. To manage and track changes in code", "D. To execute code"],
        "answer": "C"
    },
    {
        "question": "What is the main advantage of object-oriented programming (OOP)?",
        "options": ["A. Simplicity", "B. Reusability", "C. Procedural nature", "D. No need for functions"],
        "answer": "B"
    },
    {
        "question": "What is the HTTP status code for a successful response?",
        "options": ["A. 200 OK", "B. 404 Not Found", "C. 500 Internal Server Error", "D. 302 Found"],
        "answer": "A"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. NumPy", "B. Pandas", "C. Matplotlib", "D. TensorFlow"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of a constructor method in object-oriented programming?",
        "options": ["A. To create objects", "B. To destroy objects", "C. To update objects", "D. To copy objects"],
        "answer": "A"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question": "What is the result of the following Python code: `3 + '3'`?",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for developing mobile applications?",
        "options": ["A. Java", "B. Python", "C. C#", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "What is the purpose of the `if` statement in programming?",
        "options": ["A. To perform a loop", "B. To declare a function", "C. To make decisions based on conditions", "D. To define a class"],
        "answer": "C"
    },
    {
        "question": "What is the value of x, in 4x-6=2x?",
        "options": ["A. 4", "B. 6", "C. 3", "D. 1"],
        "answer": "C"
    },
    {
        "question": "Solve simultaneously: 3x + 3y=18; 5x + 3y=28",
        "options": ["A. (-5,1)", "B. (5,1)", "C. (-1,-5)", "D. (1,5)"],
        "answer": "B"
    },
    {
        "question": "Solve for y: 3y = 4 + y",
        "options": ["A. 2", "B. -3", "C. -2", "D. 0"],
        "answer": "A"
    },
    {
        "question": "Solve: 2x + 3y=13; 2x + y=7",
        "options": ["A. (4.5,2)", "B. (-4.5,3)", "C. (4,2)", "D. (4.5,-2)"],
        "answer": "D"
    },
    {
        "question": "Find the root of the quadratic equation; (4x^2) + 4x 1=0",
        "options": ["A. (0.5,0.5)", "B. (0.5,-0.5)", "C. (0.5 twice)", "D. (-0.5 twice)"],
        "answer": "D"
    },
    {
        "question": " What is the minimum and maximum value of the equation: (2x^2)-4x-2=0 ",
        "options": ["A. (-1,-4)", "B. (4,1)", "C. (1,-4)", "D. (-1,4)"],
        "answer": "C"
    },
]
#displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False
#main body
if __name__=="__main__":
    score=0
    random.shuffle(quiz_data)
    for i in range(1,16):
        print(f'Question {i} of 15')
        if ask_question(quiz_data[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

    print(f"You scored {score}/15.")