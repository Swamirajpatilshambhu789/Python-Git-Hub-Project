# Importing Module
import pyttsx3

# Setting Up 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Intro
print("Welcome to RoboSpeaker")

# Asking input
useri = input("Enter what you want me to say: ")

# Saying
engine.say(useri)
engine.runAndWait()