# Importing Moudle
import random

# Printing Intro
print("Welcome to Rock Paper Scisor")
while True:
    # Genrating num for computer turn
    compt = random.randint(1,3)

    # Asking for input
    uinp = input("Enter r for Rock and p for Paper and s for Sccisor: ")

    # Computer's number to turn
    # 1 = Rock
    # 2 = Paper
    # 3 = Sccisor

    # Comparing
    if uinp=="r":
        if compt==1:
            print(f"The comp chosed Rock")
            print("Tie")

        if compt==2:
            print(f"The comp chosed Paper")
            print("You Lost")  

        if compt==3:
            print(f"The comp chosed Sccisor")
            print("You Win")

    elif uinp=="p":
        if compt==1:
            print("The comp chosed Rock")
            print("You Win")

        if compt==2:
            print("The comp chosed Paper")
            print("Tie")

        if compt==3:
            print("the comp chosed")
            print("You Lost")  


    elif uinp=="s":
        if compt==1:
            print("The comp chosed Rock")
            print("You Lost")  

        if compt==2:
            print("The comp chosed Paper")
            print("You Win")

        if compt==3:
            print("The comp chosed Sccisor")
            print("Tie")

    else:
        print("We have no other option than Rock Paper Sccisor")
        continue 