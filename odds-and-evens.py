import random

def get_choices():
  options = ["1" , "2"]

  player_choice = input("Make your choice: ")
  computer_choice = random.choice(options)

  choices = {"player":player_choice , "computer":computer_choice}
  
  return choices

def check_win(player, computer):
  print(f"Your choice is {player}, computer's choice is {computer}.")

  if player == computer:
    return "The result is even. Evens win."
  else:
    return "The result is odd. Odds win."

choices = get_choices()
result = check_win(choices["player"] , choices["computer"])
print(result)