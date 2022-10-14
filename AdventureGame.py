#Kom ihåg att def måste vara i rätt årdning
knife = False
ruby = False
diamond = False
emerald = False


class elseWrong:
    xl = 5

wrong = elseWrong()


def classCalculate():
    if wrong.xl == 5:
        print("Please enter a valid option.")


def vaggScene():
    directions = ["dra", "fly"]
    print("Du inser att du inte har tid att få ut emeralden men din magkänsla säger åt dig att försöka.")
    print("Vill du försöka dra låss emeralden eller vill du fly?")
    userInput = ""
    while userInput not in directions:
        print("Options: dra/fly")
        userInput = input()
        if userInput == "dra":
            print("Du drar och drar och efter vad känns som en evighet kommer emeralden låss!")
            print("Hellt plötsligt känner du dig yr och du svimmar.")
            print("Du vaknar upp framför dörren igen utan några skador med emeralden i din hand.")
            emerald = True
            secondKrypt()
        elif userInput == "fly":
            print("Du försöker fly men zombiena har ringat in dig.")
            print("Du dör smärtsamt.")
            print("GAME OVER!")
            quit()
        else:
            classCalculate()


def hellHole():
    directions = ["hoppa", "slåss"]
    print("Du kan hörra ljudet av fotsteg bakom dig.")
    print("Du inser att du bara har två val.")
    userInput = ""
    while userInput not in directions:
        print("Options: hoppa/slåss")
        userInput = input()
        if userInput == "hoppa":
            print("Du hoppar ner i hållet, bara du vet vad ditt öde blev.")
            print("Highway to Hell Ending")
            quit()
        elif userInput == "slåss":
            print("Du väljer att slåss.")
            print("Utan vapen blir du dödad nästan direct. :(")
            print("GAME OVER!")
            quit()
        else:
            classCalculate()


def zombieStandOff():
    directions = ["vägg", "ljuset"]
    print("Du hör ljudet av mer zombies som kommer närmare snabbt!")
    print("Du börjar springa mot ljuset men helt plöstsligt ser du något glitra i en närra vägg!")
    userInput = ""
    while userInput not in directions:
        print("Du kan välja att springa fram till väggen och riskera att zombiena tar dig eller klara dig garanterat till ljuset.")
        print("Options: vägg/ljuset")
        userInput = input()
        if userInput == "vägg":
            print("Du springer mot väggen och när du kommer fram ser du en emerald som sitter fast i den!")
            vaggScene()
        elif userInput == "ljuset":
            print("Du kommer fram till ljuset men det var inte vad du trode!")
            print("Det vissar säg att ljuset kom från ett håll i marken från vilket det kommer en stark värme och ljus.")
            print("Du tycker också att du kan höra ljudet av skrik från hållet.")
            hellHole()
        else:
            print("Du kunde inte bestämma dig i tid och blev upäten av zombier.")
            print("GAME OVER!")
            quit()


def vansterKrypt():
    directions = ["slåss", "backåt"]
    print("Du kommer in i ett långt öppet område.")
    print("Det ser ut som en övergiven kloak.")
    print("Medans du går vidare in i kloaken ser du ett starkt varmt ljus längre fram, Det kanske är en väg ut!")
    print("Men helt plötsligt hör du ett ljud coh ser en till zombie som värckar vakta vägen ut, men denna är klädd i rustning.")
    userInput = ""
    while userInput not in directions:
        print("Options: slåss/backåt")
        userInput = input()
        if userInput == "slåss":
            print("Du besegrar zombien men din kniv går sönder i striden!")
            knife = False
            zombieStandOff()
        elif userInput == "backåt":
            print("Du går tillbaka")
            secondKrypt()
        else:
            classCalculate()


def bokScene():
    directions = ["ingenting"]
    print("Fattiga har mig, rika behöver mig. Äter du mig dör du. Vad är jag?")
    userInput = ""
    while userInput not in directions:
        print("Options: Lista ut det själv, också glöm inte att skriva svaret i små bokstäver.")
        userInput = input()
        if userInput == "ingenting":
            print("Rätt Svar!")
            print("Boken börjar bli transperant och börjar långsamnt försvinna.")
            print("När det har helt försvunit liger det kvar en diamant")
            print("Du väljer att ta med den medans du går tillbaka till dörren.")
            diamond = True
            secondKrypt()
        else:
            print("Fel svar")
            print("Du tittar up snabbt och hinner precis se en pil träfa dig i mellan ögonen.")
            print("GAME OVER!")
            quit()


def hogerKrypt():
    directions = ["boken", "backåt"]
    print("Du kommer in i ett uplyst rum med en öpen bok i mitten på en pedestal.")
    userInput = ""
    while userInput not in directions:
        print("Options: boken/backåt")
        userInput = input()
        if userInput == "boken":
            print("Du går fram till boken och hittar en gåtta i den.")
            bokScene()
        elif userInput == "backåt":
            print("Du går tillbaka")
            secondKrypt()
        else:
            classCalculate()


def skattkamare():
    directions = ["kissta", "backåt"]
    print("Inuti rummet hittar du en öppen skattkista full med guld och värdefulla stennar!")
    print("Vad vill du göra?")
    userInput = ""
    while userInput not in directions:
        print("Options: kissta/backåt")
        userInput = input()
        if userInput == "kissta":
            print("Du väljer att ta med dig kistan.")
            print("Men så fort du rör den så ser du hur en av väggarna öppnas!")
            print("Det är en vägg ut!")
            print("Gratis du flydde gråttan en rik man.")
            print("Rich Ending")
            quit()
        elif userInput == "backåt":
            print("Du går tillbaka.")
            secondKrypt()
        else:
            classCalculate()



def secondKrypt():
    directions = ["dörr", "höger", "vänster", "backåt"]
    print("Du kommer fram till en stor dörr med tre hål i sig och två vägar på varsin sida av dörren.")
    userInput = ""
    while userInput not in directions:
        print("Options: dörr/höger/vänster/backåt")
        userInput = input()
        if userInput == "dörr":
            if ruby and diamond and emerald:
                print("Dörren öppnas och du går in.")
                skattkamare()
            else:
                print("Dörren är låst.")
                secondKrypt()
        elif userInput == "höger":
            print("Du går höger")
            hogerKrypt()
        elif userInput == "vänster":
            print("Du går vänster")
            vansterKrypt()
        elif userInput == "backåt":
            print("Du går tillbaka")
            kryptScene()
        else:
            classCalculate()


def kryptScene():
    directions = ["framåt", "undersök"]
    print("Efter du besegrat zombine forsätter du framåt men medans du går faller taket in bakom dig!")
    print("Det går inte att gå tillbaka, det går bara att gå framåt.")
    userInput = ""
    while userInput not in directions:
        print("Options: framåt/undersök")
        userInput = input()
        if userInput == "framåt":
            secondKrypt()
        elif userInput == "undersök":
            print("Du söker igenom de fallna taket och hittar en rubin bland stenarna!")
            ruby = True
            kryptScene()
        else:
            classCalculate()



def zombieScene():
    directions = ["slåss","backåt"]
    print("Framför dig står det en zombie som blockerar utgången vad vill du göra?")
    userInput = ""
    while userInput not in directions:
        print("Options: slåss/backåt")
        userInput = input()
        if userInput == "slåss":
            if knife:
                print("Du attackerar zombien med en kniv och lyckas döda den.")
                kryptScene()
            else:
                print("Du attackerar zombien utan vapen och blir bitten!")
                print("GAME OVER!")
                quit()                    
        elif userInput == "backåt":
            showHogerPath()
        else:
            classCalculate()

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
            classCalculate()


def showVansterPath():
    directions = ["framåt","backåt"]
    global knife
    print("Framför dig ser du en mörk väg som efter 10m svänger höger, var vill du gå?")
    userInput = ""
    while userInput not in directions:
        print("Options: framåt/backåt")
        userInput = input()
        if userInput == "framåt":
            print("Det vissa sig att vägen bara gick till en stenvägg men i väggen ittar du en kniv! Du plåckar up kniven och väljer att gå tillbaka.")
            knife = True
            introScene()
        elif userInput == "backåt":
            print("Du väljer att gå tillbaka.")
            introScene()
        else:
            classCalculate()


def showFramatPath():
    directions = ["spring","gå"]
    print("Du följer den mörka tunneln framåt.")
    print("Efter ett tag ser du ljus och känner vind mot ditt hud, vad vill du göra?")
    userInput = ""
    while userInput not in directions:
        print("Options: spring/gå")
        userInput = input()
        if userInput == "spring":
            print("Du springer framåt så gladd att vara fri.")
            print("Men du ser inte det stora hålet i vägen och du faller ner.")
            print("GAME OVER")
            quit()
        elif userInput == "gå":
            print("Du går försiktit framåt och ser ett stort håll som blockerar utgången.")
            print("Du går försiktigt runt hålet.")
            print("Gratis du är fri!")
            print("Normal Ending")
            quit()
        else:
            classCalculate()


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
            showVansterPath()
        elif userInput == "framåt":
            showFramatPath()
        else:
            classCalculate()

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
    

