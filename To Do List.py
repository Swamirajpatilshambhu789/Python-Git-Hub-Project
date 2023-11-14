# Importing Module
from collections import Counter

# Intro
print("Welcome to Todoer.a to do aplication")

# a list to store todays task
tasks = []

while True:
    # asking for todays task
    task = input("Enter todays task(enter q to finish): ")

    # If finshed entering todays task
    if task=='q':
        break
    # Storing todays task
    tasks.append(task)

# a list to store todays task which are done
tasksdone = []

while True:
    # asking for todays task which are done
    taskdone = input("Enter tasks done: ")
    tasksdone.append(taskddone)

    # Counting list items for condition
    countsd = Counter(tasksdone)
    countss = Counter(tasks)

    # If all tasks are finshed
    if countsd==countss:
        print("Thanks for using this app.Have a nice day")
        break
        quit()
        print("Done all tasks")

