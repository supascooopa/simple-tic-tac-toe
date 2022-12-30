import numpy


def board_display(board):
    row_seperator = "---+---+---"
    for i in range(3):
        if i == 2:
            print(board_updater(board[i]))
        else:
            print(board_updater(board[i]))
            print(row_seperator)


def board_updater(row):
    # adding exes to the board
    # the left column symbol adder
    column_seperator = "   |   |   "
    column_seperator = column_seperator[:1] + row[0] + column_seperator[2:]
    # the middle column symbol adder
    column_seperator = column_seperator[:5] + row[1] + column_seperator[6:]
    # the right symbol adder
    column_seperator = column_seperator[:9] + row[2] + column_seperator[10:]
    # print(column_seperator)
    return column_seperator


# player assign symbol by writing top, middle or bottom row first. Then left, middle or right column
def checking_for_winner(symbol):
    # checking if column  has same symbol
    column_check = numpy.all(grid == symbol, axis=0)

    # checking if row has same symbol
    row_check = numpy.all(grid == symbol, axis=1)

    # creating diagonal starting from top left down to bottom right and checking for same symbol
    left_diagonal = grid.diagonal()
    left_diagonal_check = numpy.all(left_diagonal == symbol)

    # creating diagonal starting from top right down to bottom left and checking for same symbol
    right_diagonal = numpy.fliplr(grid).diagonal()
    right_diagonal_check = numpy.all(right_diagonal == symbol)
    if any(column_check) or any(row_check) or left_diagonal_check or right_diagonal_check:
        return True


# numpy array to assigning symbols
grid = numpy.array([[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]])
# a dictionary to help assign player choices on the numpy array grid
player_choices_dict = {"TL": [0, 0], "TM": [0, 1], "TR": [0, 2],
                       "ML": [1, 0], "MM": [1, 1], "MR": [1, 2],
                       "BL": [2, 0], "BM": [2, 1], "BR": [2, 2]}

symbols_list = ["X", "O"]
# a players history list to prevent overlapping choices
player_choices_hist = []
# explanation of how the game works
print("""
        Welcome to this text based simple tic-tac-toe game. The game uses regular tic-tac-toe rules,
         nothing fancy. The way the player can choose spaces is by writing the first letter name of the row and
         position of column. As an example TL will will assign the players symbol to the top left space. 
         WARNING: IF THE SPACE IS ALREADY OCCUPIED YOU CAN'T ASSIGN THE PLAYER HAS TO CHOOSE AN ALREADY UNOCCUPIED
         SPACE! 
         Here is a list of all available spaces available to the player:
          Top Left: TL
          Top Middle: TM
          Top Righ: TR
          Middle Left: ML
          Middle Middle: MM
          Middle Right: MR
          Bottom Left: BL
          Bottom Middle: BL
          Bottom Right: BR
""")
# displaying the grid to the player
board_display(grid)
game = True
while game:
    for symbol in symbols_list:
        print("It's " + symbol + "'s turn")
        player_input = input("Please choose a space: ").upper()
        # a while loop to keep players from overlapping choices
        while player_input:
            if player_input not in player_choices_hist:
                x, y = player_choices_dict[player_input]
                grid[x, y] = symbol
                board_display(grid)
                player_choices_hist.append(player_input)
                break
            else:
                board_display(grid)
                print("THAT SPACE IS ALREADY TAKEN PLEASE CHOOSE ANOTHER")
                player_input = input("Please choose a space: ").upper()
        # checking at the end of every player turn for the winner
        if checking_for_winner(symbol):
            print(f"{symbol} is the winner of the game!")
            game = False
            break
        elif " " not in grid.flat:
            print("It's a tie!")
            game = False
            break





