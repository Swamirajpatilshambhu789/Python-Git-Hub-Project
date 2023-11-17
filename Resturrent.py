class menu:
    def __init__(self, order):
        cando = {
            "butter panner":250,
                    "chicken":300,
                    "mutton":350,
                    "roti":5, 
                    "pav baji":100,
                    "pizza":200,
                    "burger":100,
                    "gulab jamun":50,
                    "kaju katli":50,
                    "water":10
                      }
        
        if order in cando:
            print(f"Here is your {order}")
            global bill
            bill = 0
            bill += cando[order]
        elif order=='q':
            print(f"{bill} is your total")
            print("Thanks for coming.Visit again")
            quit()
        else:
            print("sorry we don't make it here")

print("Welcome to sweet home")
while True:
        order = input("sir order: ")
        caller = menu(order)
