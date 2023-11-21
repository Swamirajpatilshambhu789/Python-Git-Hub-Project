 # Importing Moudle
import requests
import json

# Intro
print("Welcome to weatheraps")
while True:
    # Assking for city and state
    nameoco = input("Enter the name of the country: ")
    nameos = input(f"Enter the name of the state(in {nameoco}): ")
    nameoc = input(f"Enter the name of the city(in {nameos}): ")

    # storing api url
    url = f"http://api.weatherapi.com/v1/current.json?key=c0005a6eb1a449f3be4102524230911&q={nameoco}/{nameos}/{nameoc}"

    try:
        # Importing data from url
        r = requests.get(url)

        # Converting into dictionary
        wd = json.loads(r.text)
        
        # Printing Conditions
        print(wd["current"]["humidity"])

    except:
        print("Enter a valid place")
        continue