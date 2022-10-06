#Kom ihåg att def måste vara i rätt årdning



#inte klar måste ha zombie fight
def zombieScene():
    directions = ["slåss","backåt"]
    print("Framför dig står det en zombie som blockerar utgången vad vill du göra?")
    userInput = ""
    while userInput not in directions:
        print("Options: slåss/backåt")
        userInput = input()
        if userInput == "slåss":
            print("Insert zombie fight")
        elif userInput == "backåt":
            showHogerPath()
        else:
            print("Please enter a valid option.")

#Den högra vägen
def showHogerPath():
    directions = ["vänster","tillbaka"]
    print("Efter du gott ett tag mott höger märker du att grotten svänger vänster, när du kollar runt hörnet ser du en stor skugga, var vill du gå?")
    userInput = ""
    while userInput not in directions:
        print("Options: vänster/tillbaka")
        userInput = input()
        if userInput == "vänster":
            zombieScene()
        elif userInput == "tillbaka":
            introScene()
        else:
            print("Please enter a valid option.")

#Start scenen
def introScene():
    directions = ["höger","vänster","framåt"]
    print("Framför dig är det tre väggar som du kan gå i vilken vill du följa?")
    userInput = ""
    while userInput not in directions:
        print("Options: höger/vänster/framåt")
        userInput = input()
        if userInput == "höger":
            showHogerPath()
        elif userInput == "vänster":
            showFramatPath()
        else:
            print("Please enter a valid option.")

#introt och där man skriver sitt namn
if __name__ == "__main__":
  while True:
    print("Välkommen till spelet och lycka till")
    print("Du vaknar up i en mörk gråtta med vattendroppar som faller från taket.")
    print("Du vet ej hur du kom hit eller vägen ut.")
    print("Vad vill du göra?.")
    print("Men först av allt vad hetter du: ")
    name = input()
    print("Lycka till, " +name+ ".")
    introScene()
    

