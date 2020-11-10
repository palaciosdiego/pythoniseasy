# import termcolor
# termcolor.cprint(u"\u2B24", "red")
# termcolor.cprint(u"\u2B24", "yellow")

ROW_COUNT = 6
COLUMN_COUNT = 7

PIECE_NONE = " "
PIECE_ONE = "x"
PIECE_TWO = "o"

DIRECTIONS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def create_board(rows=ROW_COUNT, columns=COLUMN_COUNT):
    """ Creates empty board"""
    board = []

    for row in range(rows):
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
        board.append(board_row)

    return board


def print_board(board):
    """ Prints Connect 4 board """
    print(board)
    cont = 1
    for row in board:
        print("|" + "|".join(row) + "|")


def drop_piece(board, column, piece):
    """Attempts to drop specified piece into the board at the
    specified column

    If this succeeds, return True, otherwise return False.
    """
    print("column", column)
    if column >= 7:
        print("Column not valid")

        return False

    for row in reversed(board):
        if row[column] == PIECE_NONE:
            row[column] = piece
            return True

    return False


def find_winner(board, length=4):
    """ Return whether or not the board has a winner """

    rows = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == PIECE_NONE:
                continue

            if check_piece(board, row, column, length):
                return board[row][column]

    return None


def check_piece(board, row, column, length):
    """Return whether or not there is a winning sequence starting from
    this piece
    """
    rows = len(board)
    columns = len(board[0])

    for dr, dc in DIRECTIONS:
        found_winner = True

        for i in range(1, length):
            r = row + dr * i
            c = column + dc * i

            if r not in range(rows) or c not in range(columns):
                found_winner = False
                break

            if board[r][c] != board[row][column]:
                found_winner = False
                break

        if found_winner:
            return True

    return False


def HumanPlayer(board, history, players):
    """ Read move from human player """
    columns = len(board[0])
    column = -1

    while column not in range(0, columns):
        column = input("Which column? ")

    return column


Player = 1

currentBoard = create_board()
print_board(currentBoard)
Winner = None


while not Winner:
    print("Players turn: ", Player)
    MoveColumn = int(input("Please enter the column\n")) - 1
    if Player == 1:
        # Make move for p1
        move = drop_piece(currentBoard, MoveColumn, PIECE_ONE)
        if move:
            print_board(currentBoard)
            Player = 2
    else:
        # Make move for p2
        move = drop_piece(currentBoard, MoveColumn, PIECE_TWO)
        if move:
            print_board(currentBoard)
            Player = 1

    Winner = find_winner(currentBoard)

print("The winner is {}".format(Winner))
