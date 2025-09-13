import time
import pyttsx3

print("Welcome to drink water remainder")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

time.sleep(900)
engine.say("drink water")
engine.runAndWait()