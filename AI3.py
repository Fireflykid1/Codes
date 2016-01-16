print("State your Identity...")
name = input()
print("Hello, Proffesor " + name)
print('Would you like too play a game?...')
game = input ()
if game is['Yes'] or ['Sure'] or ['yes'] or ['sure']:
    print("What would you like too play?")
else:
    print("Then possibly some other time, Professor?")
options = input ()
if options is['What are the games?'] or ['what are the games?'] or ['What are the options?'] or ['what are the options?']:
    print('TicTacToe, Chess, Pacman, Mafia...')
else:
    print('I am sorry' + name + ' I do not understand what you are asking of me?')
TicTacToe = input ()
if option.lower() == "tictactoe":

import random
import sys
X = 'X'
O = 'O'
BOARD_SIZE = 3

def main():
    board = Board(BOARD_SIZE)

    for _ in range(board.size ** 2):
        board.make_move()
        board.print_board()
        winner = board.detect_winner()
        if winner is not None:
            end_game(winner)
        board.toggle_turn()

    winner = None
    end_game(winner)

class Board(object):
    def __init__(self, size, turn=None):
        self.state = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        self.turn = turn or random.choice([X, O])

    def print_board(self):
        print('\n')
        for i, row in enumerate(self.state):
            values = [item or ' ' for item in row]
            places = (' {} |' * self.size)[:-1]
            print(places.format(*values))
            if i != self.size - 1:
                print(('----' * self.size)[:-1])
        print('\n')

    def make_move(self):
        max_moves = self.size ** 2
        while True:
            prompt = 'Player {}, please enter a valid move from 1-{} using the number pad: '
            move = input(prompt.format(self.turn, max_moves))
            try:
                move = int(move)
            except ValueError:
                continue

            if move not in range(1, max_moves + 1):
                continue

            row = self.size - 1 - ((move - 1) // self.size)
            column = (move - 1) % self.size

            if self.state[row][column] is None: 
                self.state[row][column] = self.turn
                break

    def detect_winner(self):
        win_combinations = []
        win_combinations.extend([row for row in self.state])
        win_combinations.extend([list(column) for column in zip(*self.state)])
        mirrored_state = [list(reversed(item)) for item in zip(*self.state)]
        win_combinations.append([row[index] for index, row in enumerate(self.state)])
        win_combinations.append([row[index] for index, row in enumerate(mirrored_state)])

        if any(all(item is X for item in combo) for combo in win_combinations):
            winner = X
        elif any(all(item is O for item in combo) for combo in win_combinations):
            winner = O
        else:
            winner = None
        return winner

    def toggle_turn(self):
        self.turn = X if self.turn == O else O

def end_game(winner):
    if winner is None:
        output = 'The game was a draw!'
    else:
        output = 'The winner is {} !'.format(winner)
    sys.exit(output)

if __name__ == '__main__':
    main()
