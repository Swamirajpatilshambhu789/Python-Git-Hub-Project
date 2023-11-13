# Intro
print("Welcome to numebrs into roman converter")
# Making a Function for procces


def int_to_roman(num):
    # Creating a list for numbers
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # Creating a list for roman numerals
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    # Making a variable to store the ans
    roman_num = ""
    # Making a variable for taking items from val ans syb
    i = 0
    # It will run until 0 so the ans is completed
    while num > 0:
        # It will extract value from val and syb until 0
        for _ in range(num // val[i]):
            roman_num = roman_num + syb[i]
            num = num - val[i]
        i += 1
    # Retruns for the answer
    return roman_num


# Taking input
number = input("Enter a number(Enter q to quit): ")
try:
    if number == "q":
        print("Thanks for using")

        quit()

    else:
        number = int(number)


except:
    print("Please enter valid input")
# Calling function & storing return or the answer
roman_numeral = int_to_roman(number)
# Printing Output
print(f"The Roman numeral for {number} is: {roman_numeral}")
