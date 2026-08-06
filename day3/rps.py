import random

human_move = int(input("Rock(1) Paper(2) Scissor(3): "))
computer_move = random.randint(1,3)

if human_move == 1:
  print("Human - Rock")
elif human_move == 2:
  print("Human - Paper")
elif human_move == 3:
  print("Human - Scissor")
else:
  print("Bad input")

if computer_move == 1:
  print("Computer - Rock")
elif computer_move == 2:
  print("Computer - Paper")
elif computer_move == 3:
  print("Computer - Scissor")
else:
  print("Bad input")

if human_move == 1:
  if computer_move == 1:
    print("Tied")
  elif computer_move == 2:
    print("Computer wins")
  else: # if computer_move is 3
    print("Human wins")
elif human_move == 2:
  if computer_move == 1:
    print("Human wins")
  elif computer_move == 2:
    print("Tied")
  else: # if computer_move is 3
    print("Computer wins")
else: # if human_move is 3
  if computer_move == 1:
    print("Computer wins")
  elif computer_move == 2:
    print("Human wins")
  else: # if computer_move is 3
    print("Tied")