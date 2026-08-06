import random
import tkinter as tk
from tkinter import ttk


# Original game functions (unmodified)
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


MOVE_NAMES = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissors')
        self.root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

        self.build_interface()

    def build_interface(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.grid(row=0, column=0)

        title = ttk.Label(
            main_frame,
            text='Rock Paper Scissors',
            font=('Arial', 20, 'bold')
        )
        title.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        instructions = ttk.Label(main_frame, text='Choose your move:')
        instructions.grid(row=1, column=0, columnspan=3, pady=(0, 10))

        for column, move in enumerate(('r', 'p', 's')):
            button = ttk.Button(
                main_frame,
                text=MOVE_NAMES[move],
                command=lambda selected_move=move: self.play_round(selected_move)
            )
            button.grid(row=2, column=column, padx=5, ipadx=10, ipady=8)

        self.player_choice_label = ttk.Label(
            main_frame,
            text='You chose: --',
            font=('Arial', 12)
        )
        self.player_choice_label.grid(row=3, column=0, columnspan=3, pady=(20, 5))

        self.computer_choice_label = ttk.Label(
            main_frame,
            text='Computer chose: --',
            font=('Arial', 12)
        )
        self.computer_choice_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.result_label = ttk.Label(
            main_frame,
            text='Make a selection to begin.',
            font=('Arial', 14, 'bold')
        )
        self.result_label.grid(row=5, column=0, columnspan=3, pady=15)

        self.score_label = ttk.Label(main_frame, text='')
        self.score_label.grid(row=6, column=0, columnspan=3, pady=(0, 15))
        self.update_score()

        reset_button = ttk.Button(
            main_frame,
            text='Reset Score',
            command=self.reset_score
        )
        reset_button.grid(row=7, column=0, columnspan=2, padx=5)

        quit_button = ttk.Button(
            main_frame,
            text='Quit',
            command=self.root.destroy
        )
        quit_button.grid(row=7, column=2, padx=5)

    def play_round(self, player_move):
        computer_move = get_computer_move()
        winner = compute_winner(player_move, computer_move)

        self.player_choice_label.config(
            text='You chose: ' + MOVE_NAMES[player_move]
        )
        self.computer_choice_label.config(
            text='Computer chose: ' + MOVE_NAMES[computer_move]
        )

        if winner == 'player':
            self.player_score += 1
            message = 'You win!'
        elif winner == 'computer':
            self.computer_score += 1
            message = 'The computer wins!'
        else:
            self.draws += 1
            message = 'It is a draw!'

        self.result_label.config(text=message)
        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=(
                f'You: {self.player_score}    '
                f'Computer: {self.computer_score}    '
                f'Draws: {self.draws}'
            )
        )

    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0
        self.player_choice_label.config(text='You chose: --')
        self.computer_choice_label.config(text='Computer chose: --')
        self.result_label.config(text='Make a selection to begin.')
        self.update_score()


if __name__ == '__main__':
    root = tk.Tk()
    RockPaperScissorsGUI(root)
    root.mainloop()
