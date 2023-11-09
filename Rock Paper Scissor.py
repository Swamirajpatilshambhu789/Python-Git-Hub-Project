# Importing Moudle
import random

# Printing Intro
print("Welcome to Rock Paper Scisor")
while True:
    # Genrating num for computer turn
    compt = random.randint(1,3)

    # Asking for input
    uinp = input("Enter r for Rock and p for Paper and s for Sccisor")

    # Computer's number to turn
    # 1 = Rock
    # 2 = Paper
    # 3 = Scisor

    # Comparing
    if uinp=="r":
        if compt==1:
            print("Tie")

        if compt==2:
            print("You Lost")  

        if compt==3:
            print("You Win")

    if uinp=="p":
        if compt==1:
            print("You Win")

        if compt==2:
            print("Tie")

        if compt==3:
            print("You Lost")  


    if uinp=="s":
        if compt==1:
            print("You Lost")  

        if compt==2:
            print("You Win")

        if compt==3:
            print("Tie")