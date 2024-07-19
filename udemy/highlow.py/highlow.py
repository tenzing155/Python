import random
from art import logo, vs
from game_data import data


def get_random_data():
  """Get data from random account"""
  return random.choice(data)

def format_data(data):
  """Format data into printable format: name, description and country"""
  name = data["name"]
  description = data["description"]
  country = data["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_data()
  account_b = get_random_data()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_data()

    while account_a == account_b:
      account_b = get_random_data()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()




