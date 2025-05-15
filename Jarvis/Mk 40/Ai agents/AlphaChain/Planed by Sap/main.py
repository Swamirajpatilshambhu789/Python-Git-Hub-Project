import requests
import google.generativeai as genai
import os

file_path = r"D:\Swamiraj\Programing\Python\Python-Git-Hub-Project\Jarvis\Mk 40\Ai agents\AlphaChain\Planed by Sap\Trade_book.txt"

def ResponceSender(req):
    genai.configure(api_key="AIzaSyDd3i4FzfVJ0oHMkYLOHoApHl3Ao8ZXvjA")
    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    response = model.generate_content(req)
    return response.text

def Current_crypto_plan():
    with open(file_path, 'r') as file:
        file_content = file.readlines()
    buytime = file_content[0]
    buytime = ''.join(filter(str.isdigit, buytime))
    buytime = int(buytime)
    selltime = file_content[1]
    selltime = ''.join(filter(str.isdigit, selltime))
    selltime = int(selltime)
    lossmargin = file_content[2]
    lossmargin = ''.join(filter(str.isdigit, lossmargin))
    lossmargin = int(lossmargin)
    profitmargin = file_content[3]
    profitmargin = ''.join(filter(str.isdigit, profitmargin))
    profitmargin = int(profitmargin)
    currency = file_content[4]
    currencyfullform = file_content[5]
    Trade_plan = {
        "Buy price": buytime,
        "sell price": selltime,
        "loss margin": lossmargin,
        "profit margin": profitmargin,
        "currency": currency,
        "currency full form":currencyfullform
    }
    return Trade_plan

def marketvaluegetter(currency, fullform):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={fullform}&vs_currencies=usd"
    params = {"symbol": f"{currency}", "convert": "USD"}
    headers = {"X-CMC_PRO_API_KEY": "39fef9fa-3288-458e-8228-27af80da1058"}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data
 
def calculatorfromgoal(plan, current):
    On_which_stage_of_trade = int(input('''enter the nuber depending on your stage: 
                                            1.Yet to buy
                                            2.buyed
                                            3.Trade done
                                            : '''))
    if (On_which_stage_of_trade==1):
        buypricediffrence = current.get("bitcoin").get("usd")-plan["Buy price"]
        print(f"Still the price is yet to go up by {buypricediffrence}")
    
    elif(On_which_stage_of_trade==2):
        if(current.get("bitcoin").get("usd")>plan["Buy price"]):
           profitby = plan["Buy price"]-current.get("bitcoin").get("usd")
           print(f"your in profit by {profitby}")
        if(current.get("bitcoin").get("usd")<plan["Buy price"]):
           profitby = plan["Buy price"]-current.get("bitcoin").get("usd")
           print(f"your in loss by {profitby}")
        # print(f"Still the price is yet to go up by {buypricediffrence}")
    elif(On_which_stage_of_trade==3):
        print("put your next trade so i can get to work")
    

if __name__ == "__main__":
    Trade_plan = Current_crypto_plan()
    # print(Trade_plan["currency"])
    Current = marketvaluegetter(Trade_plan["currency"], Trade_plan["currency full form"])
    conclusion = calculatorfromgoal(Trade_plan, Current)