  # Project 3
  # Create a Python project to getthe value of Pi to N number of Decimal Places
  # Input a Number and the program will generate pi to the number in decimal places

from math import pi
import time
ye = ["Y", "yes", "y", "Yes"]
ne = ["N", "No", "n", "no"]

def intro():
    print("Hello My name is ADA.")
    time.sleep(2)
    pi_program()

def pi_repeat():
    answer = input("Would you like me to accept another inquiry? Y/N ")
    if answer in ye:
        pi_program()
    elif answer in ne:
        print("Glad I could help. ADA Deactivate. ")

def pi_program():
    res = input(""" Pi Decimal Place Program:
    Please input how may decimal points you want pi to be displayed to.  """)
    time.sleep(1)
    print ("Calculating inqiry of " + res + " decimal places.")
    time.sleep(2)
    print('{:.{}f}'.format(pi, res))
    time.sleep(1)
    pi_repeat()

intro()
