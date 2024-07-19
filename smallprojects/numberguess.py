#Number Guessing Game:

#Overview of the game.
import random
logo = """
 ___                      ___  _          _ _              _             
/  _>  _ _  ___  ___ ___ |_ _|| |_  ___  | \ | _ _ ._ _ _ | |_  ___  _ _ 
| <_/\| | |/ ._><_-<<_-<  | | | . |/ ._> |   || | || ' ' || . \/ ._>| '_>
`____/`___|\___./__//__/  |_| |_|_|\___. |_\_|`___||_|_|_||___/\___.|_|  
                                                                         
"""
print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")

#generating random number between 1 and 100.
num = random.randint(1, 100)
print("Pssst, The correct answer is ", num)

#choosing between easy and hard difficulty.
option = input("Choose difficulty. Type 'easy' or 'hard': ")
if option == 'easy':
    attempt = 10
elif option == 'hard':
    attempt = 5
else:
    print("Please enter correct option.")

#guessing number and implementing attempt.
while attempt > 0:
    guess = int(input("Enter your guess number:"))
    if guess > num:
        print("Too high.")
        print(f"You have {attempt} attempts remaining.")
    elif guess < num:
        print("Too low.")
        print(f"You have {attempt} attempts remaining.")
    else:
        print(f"You have guessed it correctly! {num}")
        break
    attempt -= 1   
    
    if attempt > 0:
        print("Guess again.")
    else:
        print("You've run out of attempts. You lose.")
    
