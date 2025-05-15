import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Open the file in read mode
with open('Daily Routine.txt', 'r') as file:
    for line in file:
        speak(line.strip())  # Strip removes trailing newline or spaces

