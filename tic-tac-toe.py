symbols = ['_', 'O', '_', 'X', 'X', '_', '_', 'O', 'O']

# Creating the gameboard
print("---------")
print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
print("---------")

# Creating array
a = [[symbols[0], symbols[1], symbols[2]],
    [symbols[3], symbols[4], symbols[5]],
    [symbols[6], symbols[7], symbols[8]]]

# Current gameboard situations
row_one = a[0]
row_two = a[1]
row_three = a[2]
rows = [row_one, row_two, row_three]

column_one = [a[0][0], a[1][0], a[2][0]]
column_two = [a[0][1], a[1][1], a[2][1]]
column_three = [a[0][2], a[1][2], a[2][2]]
columns = [column_one, column_two, column_three]

diagonal_one = [a[0][0], a[1][1], a[2][2]]
diagonal_two = [a[0][2], a[1][1], a[2][0]]
diagonals = [diagonal_one, diagonal_two]

# All gameboard situations
gameboard_situations = [row_one, row_two, row_three,
                    column_one, column_two, column_three,
                    diagonal_one, diagonal_two]

# Full board for comparisons
x = [['X', 'X', 'X'],
    ['X', 'X', 'X'],
    ['X', 'X', 'X']]
o = [['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']]

# Winning situations
winning_row_x = ['X', 'X', 'X']
winning_row_o = ['O', 'O', 'O']

winning_column_x = [x[0][0], x[1][0], x[2][0]]
winning_column_o = [o[0][0], o[1][0], o[2][0]]

winning_diagonal_x = [x[0][0], x[1][1], x[2][2],
                    [x[0][2], x[1][1], x[2][0]]]
winning_diagonal_o = [o[0][0], o[1][1], o[2][2],
                    [o[0][2], o[1][1], o[2][0]]]

# All winning situations
winning_situations = [winning_row_x, winning_row_o,
                    winning_column_x, winning_column_o,
                    winning_diagonal_x, winning_diagonal_o]



x_wins = False
o_wins = False
game_finished = True

if row_one == winning_row_x or row_two == winning_row_x or row_three == winning_row_x:
    x_wins = True
elif column_one == winning_column_x or column_two == winning_column_x or column_three == winning_column_x:
    x_wins = True
elif diagonal_one in winning_diagonal_x:
    x_wins = True
elif diagonal_two in winning_diagonal_x:
    x_wins = True
elif any('_' in b for b in gameboard_situations):
    game_finished = False

if row_one == winning_row_o or row_two == winning_row_o or row_three == winning_row_o:
    o_wins = True
elif column_one == winning_column_o or column_two == winning_column_o or column_three == winning_column_o:
    o_wins = True
elif diagonal_one in winning_diagonal_o:
    po_wins = True
elif diagonal_two in winning_diagonal_o:
    o_wins = True
elif any('_' in b for b in gameboard_situations):
    game_finished = False

if x_wins == True and o_wins == True:
    print("Impossible")
elif abs(symbols.count('X') - symbols.count('O')) > 1:
    print("Impossible")
elif x_wins == True:
    print("X wins")
elif o_wins == True:
    print("O wins")
elif game_finished == False:
    print("Game not finished")
elif game_finished == True:
    print("Draw")

