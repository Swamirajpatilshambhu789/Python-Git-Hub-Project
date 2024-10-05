from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
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
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

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
    if passwordebu==password:
        # play_gif()
        speak("Welcome to Jarvis(an super ai)")
        print("Welcome to Jarvis(an super ai)")
        if __name__ in "__main__":
            intro()  
            while True:
                try:
                    query = commandtaker().lower()
                except:
                    continue
                if "wikipedia" in query:
                    print("say to search in wikipedia")
                    tosearch = commandtaker()
                    # query.remove("wikipedia", "")
                    print(wikipedia.summery(tosearch))
                    speak(wikipedia.summary(tosearch))

                elif "open youtube" in query:
                    webbrowser.open("youtube.com")

                elif "open google" in query:
                    webbrowser.open("google.com")

                elif "open stack overflow" in query:
                    webbrowser.open("stackoverflow.com")

                elif "music" in query:
                    path = "C:\\Users\\admin\\Desktop\\Songs"
                    listingsongs = os.listdir(path)
                    listingsongsc = len(listingsongs)
                    rn = random.randint(0,listingsongsc-1)
                    os.startfile(os.path.join(path,listingsongs[rn]))


                elif "open vs code" in query:
                    os.startfile(os.path.join("C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"))

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
                    query = query.replace("google"," ")
                    pywhatkit.search(query)

                elif "youtube" in query:
                    query = query.replace("jarvis"," ")
                    query = query.replace("youtube", " ")
                    query = query.replace("search on", " ")
                    web = f"https://www.youtube.com/results?search_query={query}"
                    webbrowser.open(web)

                elif "news" in query:
                    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2e974d749e474183b4be750d718eed2b",
                        "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=2e974d749e474183b4be750d718eed2b",
                        "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=2e974d749e474183b4be750d718eed2b",
                        "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=2e974d749e474183b4be750d718eed2b",
                        "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2e974d749e474183b4be750d718eed2b",
                        "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2e974d749e474183b4be750d718eed2b"
                        }

                    content = None
                    url = None
                    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
                    try:
                        field = commandtaker().lower()
                    except:
                        print("Please say it again")
                        speak("Please say it again")
                    for key ,value in api_dict.items():
                        if key.lower() in field.lower():
                            url = value
                            break
                        else:
                            url = True
                    if url is True:
                        speak("Sorry we do not know about the secter you want ot know")
                    else:
                        news = requests.get(url).text
                        news = json.loads(news)
                        speak("Here is the first news.")
                        arts = news["articles"]
                        for articles in arts :
                            article = articles["title"]
                            print(article)
                            speak(article)
                            news_url = articles["url"]
                            speak("speak continue to tell you more or speak stop to end")
                            a = commandtaker()
                            if a == "continue":
                                pass
                            elif a == "stop":
                                break
                            else:
                                break
                        speak("Thanks for listening news.now continue with other facilities")
                elif "calculate" in query:
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                elif "shutdown the system" in query:
                    speak("are you sure you want to shutdown")
                    con = input("are you sure you want to shutdown: ")
                    if con=="yes":
                        speak("by my friend.see you again")
                        os.system("shutdown /s /t 1")

                    elif con=="no":
                        continue
                    
                    else:
                        continue    

                elif "schedule " in query:
                    tasks = []
                    clearornot = input("Do you want to clear your old tasks(Yes/No)")
                    if clearornot=="yes":
                        file = open("tasks.txt","w")
                        file.write(" ")
                        file.close()
                        no_of_tasks = int(input("how much tasks do you want schedule for this day"))
                        i = 1
                        for i in range(no_of_tasks):
                            tasks.append(input(f"Enter the {i} tasks"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close()
                    
                    elif clearornot=="no":
                        no_of_tasks = int(input("how much tasks do you want schedule for this day"))
                        i = 1
                        for i in range(no_of_tasks):
                            tasks.append(input(f"Enter the {i} tasks"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close()

                elif "today's task" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("sound effect nottification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=10 
                    )

                elif "game" in query:
                    while True:
                        compt = random.randint(1,3)
                        uinp = input("Enter your choice Rock(r) Paper(p) Sccisor(s) or enter q to quit")
                        if uinp=="q":
                            speak("Thanks for playing game")
                            break
                        elif uinp=="r":
                            if compt==1:
                                print("Tie")

                            if compt==2:
                                print("You Lost")  

                            if compt==3:
                                print("You Win")

                        elif uinp=="p":
                            if compt==1:
                                print("You Win")

                            if compt==2:
                                print("Tie")

                            if compt==3:
                                print("You Lost")  


                        elif uinp=="s":
                            if compt==1:
                                print("You Lost")  

                            if compt==2:
                                print("You Win")

                            if compt==3:
                                print("Tie")
                    
                        else:
                            speak("There is no other option than Rock(r) Paper(p) Sccisor(s)")

                elif "weather" in query:
                    while True:
                        try:
                            speak("What's the city name")
                            nameoc = input("Enter the city name: ")
                            speak("What's the State name")
                            nameos = input("Enter the state name: ")

                        except:
                            continue

                        url = f"http://api.weatherapi.com/v1/current.json?key=c0005a6eb1a449f3be4102524230911&q={nameos}/{nameoc}"

                        r = requests.get(url)

                        wd = json.loads(r.text)
                        try:
                            speak(wd["current"]["temp_c"],"These are in celsius")

                        except:
                            speak("Enter a valid place")
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

                elif "translate" in query:
                    translategl()
                
                elif "type" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("type","")
                    pyautogui.typewrite(query)

                elif "joke" in query:
                    limit = 1
                    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
                    response = requests.get(api_url, headers={'X-Api-Key': 'rcQCPRDdYMUZM88WTYUMVg==iJACOh0etertCVPl'})
                    if response.status_code == requests.codes.ok:
                        speak(response.text)
                    else:
                        print("Error:", response.status_code, response.text)

                elif "fact" in query:
                    category = input("Enter the catagory: ")
                    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
                    response = requests.get(api_url, headers={'X-Api-Key': 'rcQCPRDdYMUZM88WTYUMVg==iJACOh0etertCVPl'})
                    if response.status_code == requests.codes.ok:
                        speak(response.text)
                    else:
                        speak("Error:", response.status_code, response.text)
                elif "recipe" in query:
                    while True:
                        queryr = input("Enter the food name(q to quit): ")
                        if queryr=='q':
                            speak("Now enjoy with other faciliticies")
                            break
                        api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(queryr)
                        response = requests.get(api_url, headers={'X-Api-Key': 'rcQCPRDdYMUZM88WTYUMVg==iJACOh0etertCVPl'})
                        if response.status_code == requests.codes.ok:
                            speak(response.text)
                        else:
                            print("Error:", response.status_code, response.text) 

                elif "meaning" in query:
                    while True:
                        word = input("Enter the word to get the meaning(q to quit): ")
                        if word=="q":
                            speak("Now enjoy with other facilitices")
                        api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
                        response = requests.get(api_url, headers={'X-Api-Key': 'rcQCPRDdYMUZM88WTYUMVg==iJACOh0etertCVPl'})
                        if response.status_code == requests.codes.ok:
                            speak(response.text)
                        else:
                            print("Error:", response.status_code, response.text)


        
                else:
                    speak(f"jarvis don't know about it")
                    continue

        else:
            continue

        speak("You have got the jarvis password wrong 3 times so exiting the program")
        quit()