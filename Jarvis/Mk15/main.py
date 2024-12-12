# from Parts.Ai import main
import google.generativeai as genai
import keyboard
import pywhatkit
# from Parts.Face_Recognition import main
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans  # pip install googletrans
from gtts import gTTS
# import googletrans8
import pyautogui
import requests
import json
from plyer import notification
import wolframalpha
import requests
import json
import pywhatkit
import datetime
import os
import webbrowser
import random
import wikipedia
import datetime
import pyttsx3
import speech_recognition
import threading
import os

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def text_to_sentences(text):
    # Split the text by '.' and strip whitespace
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    return sentences


def queryaichecker(query):
    if "stop" "shut up" in query:
        return "continue"

def commandtakerforai():
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            voice = recognizer.listen(mic)

            text = recognizer.recognize_google(voice)
            text.lower()

            # print(f"User said: {text}")

        return text
    except:
        pass

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ResponceSender(req):
    genai.configure(api_key="AIzaSyDd3i4FzfVJ0oHMkYLOHoApHl3Ao8ZXvjA")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(req)
    res = response.text
    if "gemini" in res:
        query = query.replace("i am not gemini", "i am jarvis")
        query = query.replace("gemini", "jarvis")
    return res

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")

    if hour >= 12 and hour < 18:
        print("Good Evening")
        speak("Good evening")

    if hour >= 18:
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


def WolfRamAlpha(query):
    apikey = "WH9Y7P-W5YVQV4G3T"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(f"The answer is{result}")

    except:
        speak("The value is not answerable")


def translategl():
    speak("SURE SIR")
    print("Available languages:")
    for code, lang in googletrans.LANGUAGES.items():
        print(f"{code}: {lang}")

    translator = Translator()
    speak("Enter the language code for translation (e.g., 'hi' for Hindi)")

    while True:
        b = input("To_Lang: ").lower()

        # Check if the entered language code is valid
        if b in googletrans.LANGUAGES.keys():
            query = input("Enter text to translate: ")
            try:
                text_to_translate = translator.translate(query, dest=b, src="auto")
                translated_text = text_to_translate.text
                speakgl = gTTS(text=translated_text, lang=b, slow=False)
                speakgl.save("voice.mp3")
                # playsound("voice.mp3")  # Uncomment this if playsound is a defined function
                speak("Translation completed")
                speak("Stored in voice.mp3 please check it ")
                break
            except:
                print("Unable to translate. Please try again.")
                speak("Unable to translate. Please try again.")
        else:
            print("Invalid language code. Please choose a valid language code.")
            speak("Invalid language code. Please choose a valid language code.")


for i in range(3):
    password = "shambhu@7890"
    speak(f"You have only 3 chances to enter the password")
    print(f"You have only 3 chances to enter the password")
    passwordebu = input("Enter the password: ")
    if passwordebu == password:
        # play_gif()
        speak("Welcome I am Jarvis(an ai)")
        print("Welcome I am  Jarvis(an ai)")
        if __name__ in "__main__":
            intro()
            while True:
                try:
                    query = commandtaker().lower()

                except:
                    continue

                if "open youtube" in query:
                    webbrowser.open("youtube.com")

                elif "open google" in query:
                    webbrowser.open("google.com")

                elif "open stack overflow" in query:
                    webbrowser.open("stackoverflow.com")



                elif "open vs code" in query:
                    os.startfile(os.path.join(
                        "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"))

                elif "what's the time" in query:
                    now = datetime.datetime.now()
                    timesg = now.strftime("%H:%M:%S")
                    speak(f"The time is {timesg}")


                elif "what's the date" in query:
                    now = datetime.datetime.now()
                    datesg = now.strftime("%Y-%m-%d")
                    speak(f"The date is {datesg}")

                elif "google" in query:
                    query = query.replace("search on", " ")
                    query = query.replace("google", " ")
                    pywhatkit.search(query)


                elif "shutdown the system" in query:
                    speak("are you sure you want to shutdown")
                    con = input("are you sure you want to shutdown: ")
                    if con == "yes":
                        speak("by my friend.see you again")
                        os.system("shutdown /s /t 1")

                    elif con == "no":
                        continue

                    else:
                        continue

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    speak("smile")
                    pyautogui.sleep(5)
                    pyautogui.press("enter")

                elif "type" in query:
                    query = query.replace("jarvis", "")
                    query = query.replace("type", "")
                    pyautogui.typewrite(query)

                elif "play on Youtube" in query:
                    query = query.replace("jarvis", " ")
                    query = query.replace("youtube", " ")
                    query = query.replace("search on", " ")
                    pywhatkit.playonyt(query)

                elif "stop"in query:
                    speak("Ok sir")
                    continue

                    

                # elif "routine" in query:
                #     with open('Daily Routine.txt', 'r') as file:
                #         for line in file:
                #             speak(line.strip())
                    

                elif "make a project" in query:

                    try:
                        speak("Sir What is the name of the project")
                        nameofpro = commandtaker()
                        speak("Sir what is the type of project is it a website or python project")
                        querytype = commandtaker().lower()
                        if "python" in querytype:
                            folder_path = f"D:\Swamiraj\Programing\Projects\Python\{nameofpro}"
                            os.mkdir(folder_path)
                        if "website" in querytype:
                            folder_path = f"D:\Swamiraj\Programing\Projects\Website\{nameofpro}"
                            os.mkdir(folder_path)
                    except:
                        continue

                else:
                    res = ResponceSender(query)
                    if "." in res:
                        breakingpoint = text_to_sentences(res)
                        mornno = 1
                        while True:
                            speak(breakingpoint[0])
                            # speak(breakingpoint[1])
                            breakingpointcounter = len(breakingpoint)
                            if breakingpointcounter>mornno:
                                try:
                                    speak("If you want more information speak more and if you want to quit speak quit ")
                                    morn = commandtaker().lower()
                                    if morn == "more":
                                        speak(breakingpoint[mornno])
                                        mornno += 1
                                        continue
                                    else:
                                        break
                                except:
                                    continue
                            else:
                                break

                        continue

                    else:
                        speak(res)
                        continue



        else:
            continue

        speak("You have got the jarvis password wrong 3 times so exiting the program")
        quit()

