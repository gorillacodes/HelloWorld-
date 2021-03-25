from random import randint
import time

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))
print ("Let's Play Ship Search. You have 4 tries. Good luck!")
print()
print_board(board)
print()

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range (4):
    print()
    print ("Turn", turn + 1, "out of 4")
    print()
    
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    print()
    print ("Searching at row", guess_row, "and Col", guess_col , "...")
    time.sleep(2)
    print()

    if (ship_row == guess_row and ship_col == guess_col):
        print ("Congratulations! You found the ship!")
        print()
        break

    else:
        if (guess_row > 4 or guess_row < 0) or (guess_col > 4 or guess_row < 0):
            print ("Damn! That's not even in the ocean!!")
            print()

        elif (board[guess_row][guess_col] == "X"):
            print ("Oh come on! You have guessed that one already!!")
            print()
        else:
            print ("You missed the ship.")
            board[guess_row][guess_col] = "X"
            print()
        if turn == 3:
            print ("Game Over! You ran out of tries.")

    print_board(board)
    print()

input("Hit ENTER to exit")
