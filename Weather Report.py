 # Importing Moudle
import requests
import json

# Intro
print("Welcome to weatheraps")

# Assking for city and state
nameoc = input("Enter the name of the city(in india): ")
nameos = input("Enter the name of the state(in india): ")

# storing api url
url = f"http://api.weatherapi.com/v1/current.json?key=c0005a6eb1a449f3be4102524230911&q={nameoc}/{nameos}"

# Importing data from url
r = requests.get(url)

# Converting into dictionary
wd = json.loads(r.text)

# Printing Conditions
print(wd["current"]["temp_c"],"These are in celsius")