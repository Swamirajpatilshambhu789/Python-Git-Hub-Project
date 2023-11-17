import datetime
import os
import webbrowser
import random
import wikipedia
import pyttsx3
import speech_recognition
import datetime
recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning")

    if hour>=12 and hour<18:
        print("Good Evening")
        speak("Good evening")

    if hour>=18:
        print("Good afternoon")
        speak("Good afternoon")

    speak("i am jarvis please tell me how may i help you")
    print("i am jarvis please tell me how may i help you")

def commandtaker():
        try:
            with speech_recognition.Microphone() as mic:
                print("Lintening:")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                voice = recognizer.listen(mic)

                text = recognizer.recognize_google(voice)
                text.lower()

                print(f"User said: {text}")

            return text
        except:
            return print("Please Say it again")

if __name__=="__main__":
    intro()
    while True:
        try:
            query = commandtaker().lower()
        except:
            continue
        print(query)
        if "wikipedia"==query:
            print("say to search in wikipedia")
            tosearch = commandtaker()
            # query.remove("wikipedia", "")
            print(wikipedia.summery(tosearch))
            speak(wikipedia.summary(tosearch))

        elif "open youtube"==query:
            webbrowser.open("youtube.com")

        elif "open google"==query:
            webbrowser.open("google.com")

        elif "open stack overflow"==query:
            webbrowser.open("stackoverflow.com")

        elif "play music"==query:
            path = "C:\\Users\\admin\\Desktop\\Songs"
            listingsongs = os.listdir(path)
            listingsongsc = len(listingsongs)
            rn = random.randint(0,listingsongsc-1)
            os.startfile(os.path.join(path,listingsongs[rn]))


        elif "open vs code"==query:
            os.startfile(os.path.join("C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"))

        elif "what's the time"==query:
            now = datetime.datetime.now()
            timesg = now.strftime("%H:%M:%S")
            speak(f"The time is {timesg}")

        elif "what's the date"==query:
            now = datetime.datetime.now()
            datesg = now.strftime("%Y-%m-%d")
            speak(f"The date is {datesg}") 
        elif "shutdown"==query:
            os.startfile(os.path.join("Desktop\\shutdown"))
        else:
            speak(f"jarvis don't know about it")
            continue