# Importing Module
import time
import pyttsx3

# Intro
print("Welcome to drink water remainder")

# Setting Up 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# makes the program stop for 15 minutes(the value in time.sleep is in second)
time.sleep(900)

# Saying
engine.say("drink water")
engine.runAndWait()