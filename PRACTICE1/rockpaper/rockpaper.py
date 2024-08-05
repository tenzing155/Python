from art2 import rock,paper,scissors
import random
# User
input = int(input("Enter 0 for Rock, 1 for paper and 2 for Scissors?: "))
print("You choose:")
if input == 0:
  print(rock)
  print("Rock \n")
elif input == 1:
  print(paper)
  print("Paper \n")
elif input == 2:
  print(scissors)
  print("Scissors \n" )

#Computer
computer = random.randint(0,2)
print("Computer choose: \n")
if computer == 0:
  print(rock)
  print("Rock\n")
elif computer == 1:
  print(paper)
  print("Paper\n")
elif computer == 2:
  print(scissors)
  print("Scissors\n")

#Condition
#Rock
if input == 0 and computer == 0: 
  print("Draw.")
if input == 0 and computer == 1:
  print("Computer wins.")
if input == 0 and computer == 2:
  print("You win.")
#Paper
if input == 1 and computer == 1: 
  print("Draw.")
if input == 1 and computer == 0:
  print("You win.")
if input == 1 and computer == 2:
  print("Computer wins.")
#Scissors
if input == 2 and computer == 2: 
  print("Draw.")
if input == 2 and computer == 0:
  print("Computer wins.")
if input == 2 and computer == 1:
  print("You win.")

