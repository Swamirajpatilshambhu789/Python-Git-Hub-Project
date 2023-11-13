# Importing Module
import random

# Intro
print("Welcome to password Genrater")

# Genrating number
number1 = random.randint(1,10000)
number2 = random.randint(1,10)
number3 = random.randint(500,1000)

# Making a empty string
password = ""

# Converting integer into string to add into password
number1 = str(number1) 
number2 = str(number2)
number3 = str(number3)

# Adding number into password
password += number1
password += number2
password += number3

# Genrating number for symbol
symbol1 = random.randint(1,5)
symbol2 = random.randint(1,5)
symbol3 = random.randint(1,5)

# Genrating number for string
string1 = random.randint(1, 5)
string2 = random.randint(1, 5)
string3 = random.randint(1, 5)

# Conditioning
if symbol1==1:
    password += "!"

if symbol1==2:
    password += "@"

if symbol1==3:
    password += "#"

if symbol1==4:
    password += "%"

if symbol1==5:
    password += "&"

if symbol2==1:
    password += "!"

if symbol2==2:
    password += "@"

if symbol2==3:
    password += "#"

if symbol2==4:
    password += "%"

if symbol2==5:
    password += "&"

if symbol3==1:
    password += "!"

if symbol3==2:
    password += "@"

if symbol3==3:
    password += "#"

if symbol3==4:
    password += "%"

if symbol3==5:
    password += "&"


if string1==1:
    password += "rthferhg"

if string1==2:
    password += "dgsuighs"

if string1==3:
    password += "rdfghiidufh"

if string1==4:
    password += "dsfgnshginnsdjfno;"

if string1==5:
    password += "rrgnhg;sigh"

if string2==1:
    password += "rthferhg"

if string2==2:
    password += "dgsuighs"

if string2==3:
    password += "rdfghiidufh"

if string2==4:
    password += "dsfgnshginnsdjfno;"

if string2==5:
    password += "rrgnhg;sigh"

if string3==1:
    password += "rthferhg"

if string3==2:
    password += "dgsuighs"

if string3==3:
    password += "rdfghiidufh"

if string3==4:
    password += "dsfgnshginnsdjfno;"

if string3==5:
    password += "rrgnhg;sigh"

print(f"The Password is: {password}")