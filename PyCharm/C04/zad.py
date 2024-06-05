import random


def readnum(text):
    try:
        return int(input(text))
    except ValueError:
        print("Provided value was not integer, please enter integer")
        return readnum(text)


def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == len(board[i]) - 1:
                print(" " + board[i][j] + " ")
            else:
                print(" " + board[i][j] + " |", end="")
        if i != len(board) - 1:
            print("-" * (len(board[i]) - 1) + "---" * (len(board[i])))


def checkboard(char):
    for i in range(len(board)):
        # cheking column
        counter = 0
        for j in range(len(board)):
            if board[i][j] == char:
                counter += 1
        if counter == len(board):
            return True

        counter = 0
        for j in range(len(board)):
            if board[j][i] == char:
                counter += 1
        if counter == len(board):
            return True

    counter = 0
    for i in range(len(board)):
        if board[i][i] == char:
            counter += 1
    if counter == len(board):
        return True

    counter = 0
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] == char:
            counter += 1
    if counter == len(board):
        return True


def computermove(board, char):
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board) - 1)
    while board[y][x] != " ":
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
    board[y][x] = char
    return board

def play(board):
    while True:
        x = readnum("Enter x coordinate from upper left: ")
        while x >= len(board):
            x = readnum("Invalid coordinate, enter number between 0 and " + str(len(board) - 1) + ": ")

        y = readnum("Enter y coordinate from upper left: ")
        while y >= len(board):
            y = readnum("Invalid coordinate, enter number between 0 and " + str(len(board) - 1) + ": ")

        char = input("Enter character to place on the board (o/x): ")
        while char != "o" and char != "x":
            char = input("Enter character to place on the board (o/x): ")
        char2 = "o"
        if char == "o":
            char2 = "x"

        if board[y][x] == " ":
            board[y][x] = char
            printboard(board)
            if checkboard(char):
                print("Player '" + char + "' won.")
                break
            board = computermove(board, char2)
            print("Computer's move:")
            printboard(board)
            if checkboard(char2):
                print("Player '" + char2 + "' won.")
                break
        else:
            print("Can't place character here, cell is already occupied")

        decision = input("Would you like to continue playing? (y/n): ")
        if decision == "n":
            break
    return board


board = []
row = []
n = readnum("Enter board dimension: ")

for i in range(n):
    row.append(" ")
for i in range(n):
    board.append(row.copy())

printboard(board)
board = play(board)
