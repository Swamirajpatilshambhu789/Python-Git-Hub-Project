class ibp:
    def __init__(self, name, sallery, perfomncerate):
        # self means the variable name who has called it
        self.name = name
        self.sallery = sallery
        self.performancerate = perfomncerate

        # Conditioning
        if perfomncerate<100:
            if perfomncerate<5:
                print("No incriminating")
            if perfomncerate<10 and perfomncerate>=5:
                salleryi = sallery*0.9
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=10 and perfomncerate<20:
                salleryi = sallery*1.5
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=20 and perfomncerate<30:
                salleryi = sallery*1.9
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=30 and perfomncerate<40:
                salleryi = sallery*2
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=40 and perfomncerate<50:
                salleryi = sallery*2.2
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=50 and perfomncerate<60:
                salleryi = sallery*3.4
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=60 and perfomncerate<70:
                salleryi = sallery*3.9
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=70 and perfomncerate<80:
                salleryi = sallery*4.1
                print(f"The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=80 and perfomncerate<90:
                salleryi = sallery*4.8
                print("The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=90 and perfomncerate<100:
                salleryi = sallery*5
                print("The incriminated sallery of {name} is {salleryi}")
            
            if perfomncerate>=100:
                print("Enter the performance rate between 1 to 100")
                        
        else:
            print("Enter performancerate in between 1 to 100")

# Intro
print("Welcome to incriminatingbyperformance converter")
try:
    # Can make Take out the incriminating how many times i want
    while True:
        # Asking for name
        name = input("Enter your name(enter q to quit): ")

        # To quit 
        if name=='q':
            print("Thanks for using this app.Have a nice day")
            break
            quit()

        # Asking for sallery
        sallery = int(input("Enter your sallery: "))

        # Asking for performancerate
        performancerate = int(input("Enter your performancerate: "))

        # Calling function
        sibp = ibp(name, sallery,performancerate)

# Handling Error
except:
    print("Enter valid input")