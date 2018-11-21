import random
import time
import sys
# Program allows user to select and roll dice of varying sizes (d4, d6, d8, d10, d12, d20, d100)

# Seperate functions for all 7 types of dice
def d_four():
    x = random.randint(1,4)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_four()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_six():
    x = random.randint(1,6)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_six()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_eight():
    x = random.randint(1,8)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_eight()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_ten():
    x = random.randint(1,10)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_ten()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_twelve():
    x = random.randint(1,12)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_twelve()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_twenty():
    x = random.randint(1,20)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_twenty()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

def d_hundred():
    x = random.randint(1,100)
    print("Rolling...")
    time.sleep(3)
    print(x)
    time.sleep(1)
    option = input("Would you like to reroll (R), select a different die (D) or exit the program (X)?")
    if option == "R" or option == "r": # Reroll
        d_hundred()
    elif option == "D" or option == "d": # Pick a new dice
        reroll_menu()
    elif option == "X" or option == "x": # End program
        sys.exit()
    print(option)

# The menu the user is redirected to if they select a different die to roll

def reroll_menu():
    selected_die = input("Which die would you like to roll(d4, d6, d8, d10, d12, d20, d100)? ")
    print(selected_die)
    if selected_die == "d4" or selected_die == "D4":
        d_four()
    elif selected_die == "d6" or selected_die == "D6":
        d_six()
    elif selected_die == "d8" or selected_die == "D8":
        d_eight()
    elif selected_die == "d10" or selected_die == "D10":
        d_ten()
    elif selected_die == "d12" or selected_die == "D12":
        d_twelve()
    elif selected_die == "d20" or selected_die == "D20":
        d_twenty()
    elif selected_die == "d100" or selected_die == "D100":
        d_hundred()
    else:
        print("Error: Die not recognised")

# First menu

def menu():
    selected_die = input("Welcome to Dice Generator! Which die would you like to roll(d4, d6, d8, d10, d12, d20, d100)? ")
    print(selected_die)
    if selected_die == "d4" or selected_die == "D4":
        d_four()
    elif selected_die == "d6" or selected_die == "D6":
        d_six()
    elif selected_die == "d8" or selected_die == "D8":
        d_eight()
    elif selected_die == "d10" or selected_die == "D10":
        d_ten()
    elif selected_die == "d12" or selected_die == "D12":
        d_twelve()
    elif selected_die == "d20" or selected_die == "D20":
        d_twenty()
    elif selected_die == "d100" or selected_die == "D100":
        d_hundred()
    else:
        print("Error: Die not recognised")

menu()

