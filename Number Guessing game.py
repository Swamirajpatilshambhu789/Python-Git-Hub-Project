import random
randnum = random.randint(1, 100)

Highscore = 0

print("Welcome to the guessing game!")
while True:
  Highscore = Highscore + 1
  guesse = input("Enter the number between 1 and 100(Enter q to quit): ")

  if guesse == "q":
    print("Thanks for playing the game")
    break
    quit()

  try:
  
    guesse = int(guesse)
  except:
    print("Enter vaild number")
    continue

  if guesse == randnum:
    print(f"Congratulations! You guessed the number! in {Highscore}")
  
    refile = open(f"Highscore.txt", "r")
    rline = refile.readline() 
    rline = int(rline)
    if Highscore < rline:
    
      Highscore = str(Highscore)
      file = open("Highscore.txt", "w")
      file.write(Highscore)
    randnum = random.randint(1, 100)

  else:
    if randnum > guesse:
      print("The number is greater than your guess.")
    else:
      print("The number is less than your guess.")

