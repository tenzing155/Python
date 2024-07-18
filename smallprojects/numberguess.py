#Number Guessing Game Objectives:

# Include an ASCII art logo.
logo = """
 ___                      ___  _          _ _              _             
/  _>  _ _  ___  ___ ___ |_ _|| |_  ___  | \ | _ _ ._ _ _ | |_  ___  _ _ 
| <_/\| | |/ ._><_-<<_-<  | | | . |/ ._> |   || | || ' ' || . \/ ._>| '_>
`____/`___|\___./__//__/  |_| |_|_|\___. |_\_|`___||_|_|_||___/\___.|_|  
                                                                         
"""
print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")
import random

num = random.randint(1, 100)
print("Pssst, The correct answer is ", num)

# Allow the player to submit a guess for a number between 1 and 100.
option = input("Choose difficulty. Type 'easy' or 'hard': ")
if option == 'easy':
    i = 0
    while i < 10:
        print("You have 10 attempts remaining to guess the number.")
        print("Make a guess: ")
        guess = int(input())
        if guess < num:
            print("Too low.")
            print("Guess again.")
        elif guess > num:
            print("Too high.")
            print("Guess again.")
        else:
            print("Correct answer!", num)
            exit()
    i += 1
elif option == 'hard':
    i = 0
    while i < 5:
        print("You have 5 attempts remaining to guess the number.")
        print("Make a guess: ")
        guess = int(input())
        if guess < num:
            print("Too low.")
            print("Guess again.")
        elif guess > num:
            print("Too high.")
            print("Guess again.")
        else:
            print("Correct answer!", num)
            exit()
    i += 1
else:
    print("Please choose correct option.")