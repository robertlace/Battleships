from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Lass uns Schiffeversenken spielen!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print ""
    print "Turn: ", turn + 1
    guess_row = int(raw_input("Rate eine Reihe:"))
    guess_col = int(raw_input("Rate eine Zeile:"))
    print ""
    if guess_row == ship_row and guess_col == ship_col:
        print "Super! Du hast mein Schiff versenkt und damit gewonnen!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Ooooops, die Koordinate %s / %s befindet sich nicht im Ozean ^^" %(guess_row, guess_col)
        elif(board[guess_row][guess_col] == "X"):
            print "Diese Koordinate hast du schonmal geraten"
        else:
            print "Du hast mein Schiff verfehlt!"
            board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 3:
            print ""
            print "Game Over"
