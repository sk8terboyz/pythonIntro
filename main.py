from fractions import Fraction
import math

#Question 1
def turingTest():
    ignore = raw_input("What is your problem? ")
    response = raw_input("Have you had this problem before (yes or no)? ")
    if response == "yes":
        print("Well you have it again.")
    elif response == "no":
        print("Well, you have it now.")
    else:
        print("That wasn't 'yes' or 'no' so I cannot respond properly.")

#Answers to question 1

#Does this exhibit intelligence
# No, I do not believe this does

#Why or why not?
# Intelligence is immediately forgotten by the user once the 3 printed responses from the program and it has nothing more to say.
#Intelligence means being able to understand what is happening and react in a way you find suitable.
#The program has no intelligence after it prints out the statements programmed into it

#Question #2
def tempConverter():
    temp = input("Enter your temperature in Farenheit ")
    converted = int(round(temp+32) * Fraction(5,9))
    degreeSign = u"\N{DEGREE SIGN}"
    print (temp, degreeSign,"F =",converted,degreeSign,"C")

#Question #3
def hypotenuse():
    a = input("What is a = ? ")
    b = input("What is b = ? ")
    c = math.sqrt((a**2)+(b**2))
    formatC = "{:.2f}".format(c)
    print ("The hypotenuse is",formatC)

#Menu
def menu():
    request = int(raw_input("Which would you like to test?\n(1) Turing Test\n(2) Temperature Converter\n(3) Hypotenuse\n"))
    if request == 1:
        turingTest()
    elif request == 2:
        tempConverter()
    elif request == 3:
        hypotenuse()
    else:
        print ("You did not pick an option. Terminating")
menu()
