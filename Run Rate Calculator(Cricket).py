# Intro
print("Welcome to runrate teller")

try:
    while True:
        # Asking for score
        score = input("Enter the score(Enter q to quit): ")

        # If user wants to quit
        if score=="q":
            print("Thanks for using. Have a nice day")
            break
            quit()

        score = int(score)

        # Asking for overs
        overs = int(input("Enter How many overs were there: "))

        # Finding the output
        runrate = score/overs

        # Printing the Output
        print(runrate)

# Handling Error
except:
    print("Enter valid input")