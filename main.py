import numpy

the_ex = "X"
the_oh = "O"
row_seperator = "---+---+---"
column_seperator = "   |   |   "
# displaying the empty board to players
for i in range(3):
    if i == 2:
        print(column_seperator)
    else:
        print(column_seperator)
        print(row_seperator)

# adding exes to the board
# the left column symbol adder
column_seperator = column_seperator[:1] + the_ex + column_seperator[2:]
# the middle column symbol adder
column_seperator = column_seperator[:5] + the_ex + column_seperator[6:]
# the right symbol adder
column_seperator = column_seperator[:9] + the_ex + column_seperator[10:]
print(column_seperator)

# numpy array to assigning symbols
grid = numpy.array([["", "", ""],
                    ["", "", ""],
                    ["", "", ""]])
grid[0, 0] = "x"
grid[1, 0] = "x"
grid[2, 0] = "x"
grid[0, 1] = "x"
grid[0, 2] = "x"
print(grid)

# checking if column  has same symbol
column_check = numpy.all(grid == "x", axis=0)

# checking if row has same symbol
row_check = numpy.all(grid == "x", axis=1)

# creating diagonal starting from top left down to bottom right and checking for same symbol
left_diagonal = grid.diagonal()
left_diagonal_check = numpy.all(left_diagonal == "x")

# creating diagonal starting from top right down to bottom left and checking for same symbol
right_diagonal = numpy.fliplr(grid).diagonal()
right_diagonal_check = numpy.all(right_diagonal == "x")


# to play game
# player assign symbol by writing top, middle or bottom row first. Then left, middle or right column
player_choices_dict = {"TL": [0, 0], "TM": [0, 1], "TR": [0, 2],
                       "ML": [1, 0], "MM": [1, 1], "MR": [1, 2],
                       "BL": [2, 0], "BM": [2, 1], "BR": [2, 2]}
while True:

    player_input = input("Please choose a space: ")
    print(player_choices_dict[player_input])
