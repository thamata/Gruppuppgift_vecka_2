def main():
    
    questions = [
        "How do you demarcate a block of code in Python?",
        "What is the last version number of Python 2.X, the previous implementation of Python?",
        "What is The Zen of Python?",
        "Where does the name Python come from?",
    ]

    answers = [
        "B",
        "C",
        "A", 
        "A",
    ]

    options = [
        [
            "A. By enclosing it in angle brackets <...>.", 
            "B. By indenting the code.", 
            "C. By calling Bengt Magnusson and asking nicely.", 
            "D. By enclosing it in curly braces {...}.",
        ],
        [
            "A. 2.5", 
            "B. 2.9", 
            "C. 2.7", 
            "D. 2.99",
        ],
        [
            "A. A collection of guidelines for writing Python according to python's own design priciples.", 
            "B. A mental state you reach by praying to the creator Guido van Rossum.", 
            "C. A third party web dev framework which provides easy to use classes to force well designed code.", 
            "D. A book about why the simplicity of python made it so popular.",
        ],
        [
            "A. From the British comedy group Monty Python.", 
            "B. From the snake.", 
            "C. From the roller coaster Python in the Efteling amusement park in the Netherlands, where Guido van Rossum, the creator of Python is from.", 
            "D. It was inspired by Python of Catana, a poet who accompanied Alexander the Great.",
        ],
    ] 

    points = 0
    qNum = 0
    
    for question in questions:
        print("____________________________________________________")
        print(question)
        for option in options[qNum]:
            print(option)

        answer = input("\nPlease enter your answer A, B, C or D: ")
        print(f"You entered {answer}\n")
        if answer.upper().strip() in answers[qNum]:
            points += 1
            print("Correct answer!\nYou get a point.")
            print(f"Your score is now {points}")
        else:
            print("Wrong answer! No points for you.")

        qNum += 1
        

main()