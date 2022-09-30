def question(info_text, ans1, ans2, ans3, ans4, answer, answer2, type):
    print(info_text)
    if(len(ans1) > 0):
        print("1:", ans1)
    if(len(ans2) > 0):
        print("2:", ans2)
    if(len(ans3) > 0):
        print("3:", ans3)
    if(len(ans4) > 0):
        print("4:", ans4)

    print("Skriv rätt svar:")
    if(type == int):
        question_int(answer, answer2)
    elif(type == str):
        question_str(answer, answer2)


def question_int(answer, answer2):
    answer_input = int(input())
    if(answer == answer_input or answer2 == answer_input):
        print("Rätt")
    else:
        print("fel")

def question_str(answer, answer2):
    answer_input = input()
    if(answer == answer_input or answer2 == answer_input):
        print("Rätt")
    else:
        print("fel")

question("Vad är python?", "Ett programmeringsspråk", "En läsktillverkare", "Apollo space program", "En orm", 1, 4, int)
question("Vilket typ av programmeringsspråk är python?", "Low level", "High level","" ,"" , 2, 2, int)
question("Vilket år släpptes python?","","","","", 1991, 1991, int)
question("Vilken symbol skriver man om man vill kommentera?", "?", "-", "#", "!", 3, 3, int)
question("Vad heter skaparen av python?", "", "", "", "", "Guido van Rossum", "guido van rossum", str)