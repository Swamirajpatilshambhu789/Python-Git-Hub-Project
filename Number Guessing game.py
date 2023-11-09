# Importing Moudle
import random

# Genrates Number
randnum = random.randint(1, 100)

# Counts Highscore
Highscore = 0

while True:
  # adds Highscore
  Highscore = Highscore + 1

  # Intro
  print("Welcome to the guessing game!")

  # Asking for input
  guesse = input("Enter the number between 1 and 100(Enter q to quit): ")

  # Checking if user wants to quit
  if guesse == "q":
    print("Thanks for playing the game")
    break
    quit()

  # To counter error
  try:
    # Converts str input by user into number for cheaking
    guesse = int(guesse)
  except:
    print("Enter vaild number")
    continue

  # Cheaking
  if guesse == randnum:
    print(f"Congratulations! You guessed the number! in {Highscore}")
    # Reads file to cheak highscore to change
    refile = open(f"Highscore.txt", "r")
    rline = refile.readline()  # Reads a single line
    rline = int(rline)
    if Highscore < rline:
      # Writes highscore in file
      Highscore = str(Highscore)
      file = open("Highscore.txt", "w")
      file.write(Highscore)
    randnum = random.randint(1, 100)
  # If user doosen't get it right it helps
  else:
    if randnum > guesse:
      print("The number is greater than your guess.")
    else:
      print("The number is less than your guess.")

