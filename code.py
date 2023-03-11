squares = [' ']*9
gamers = 'XO'
board = '''
  0   1   2
  {0} | {1} | {2}
 -----------
3 {3} | {4} | {5} 5
 -----------
  {6} | {7} | {8}
  6   7   8
'''
condition_to_win = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
    (0, 4, 8), (2, 4, 6)             # diagonals
]

def wincheck(gamers):
    for a, b, c in condition_to_win:
        if {squares[a], squares[b], squares[c]} == {gamers}:
            return True

while True:
    print(board.format(*squares))
    if wincheck(gamers[1]):
        print(f'{gamers[1]} is the winner!')
        break
    if ' ' not in squares:
        print('Cats game!')
        break
    move = input(f'{gamers[0]} to move [0-8] > ')
    if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
        print('Invalid move!')
        continue
    squares[int(move)], gamers = gamers[0], gamers[::-1]
