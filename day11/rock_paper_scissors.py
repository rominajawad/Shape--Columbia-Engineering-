import random

def get_computer_move():
  return random.choice(['r','p','s'])

def get_player_move():
  while True:
    player_move = input('Please select r/p/s/q? ')
    if player_move == 'r' or player_move == 'p' or \
       player_move == 's' or player_move == 'q':
      return player_move

def compute_winner(player_move, computer_move):
  if player_move == computer_move:
    return 'draw'
  elif (player_move == 'r' and computer_move == 'p') or \
       (player_move == 'p' and computer_move == 's') or \
       (player_move == 's' and computer_move == 'r'):
       return 'computer'
  else:
    return 'player'

if __name__ == '__main__':
  while True:
    # Get player move
    player_move = get_player_move()
    if player_move == 'q':
      break
    print('You chose:',player_move)
    # Get computer move
    computer_move = get_computer_move()
    print('Computer chose',computer_move)
    # Compute winner
    winner = compute_winner(player_move, computer_move)
    print('The winner is',winner)
  

  print("Goodbye")