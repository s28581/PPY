import random


def readnum(text):
    try:
        return int(input(text))
    except ValueError:
        print("Provided value was not integer, please enter integer")
        return readnum(text)


class TicTacToeBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

    def printboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j == len(self.board[i]) - 1:
                    print(" " + self.board[i][j] + " ")
                else:
                    print(" " + self.board[i][j] + " |", end="")
            if i != len(self.board) - 1:
                print("-" * (len(self.board[i]) - 1) + "---" * (len(self.board[i])))

    def placechar(self, x, y, char):
        self.board[y][x] = char

    def getcell(self, x, y):
        return self.board[y][x]


class TicTacToeGame:
    def __init__(self, board_size, player):
        self.tictactoe_board = TicTacToeBoard(board_size)
        if player != "o" and player != "x":
            raise Exception("Player must be 'o' or 'x'")
        self.player = player
        self.computer = "x"
        if self.player == "x":
            self.computer = "o"
        self.result = "Game in progress"

    def checkboard(self, char):
        for i in range(self.tictactoe_board.size):
            # cheking column
            counter = 0
            for j in range(self.tictactoe_board.size):
                if self.tictactoe_board.getcell(j, i) == char:
                    counter += 1
            if counter == self.tictactoe_board.size:
                return True

            counter = 0
            for j in range(self.tictactoe_board.size):
                if self.tictactoe_board.getcell(j, i) == char:
                    counter += 1
            if counter == self.tictactoe_board.size:
                return True

        counter = 0
        for i in range(self.tictactoe_board.size):
            if self.tictactoe_board.getcell(i, i) == char:
                counter += 1
        if counter == self.tictactoe_board.size:
            return True

        counter = 0
        for i in range(self.tictactoe_board.size):
            if self.tictactoe_board.getcell((self.tictactoe_board.size - 1 - i), i) == char:
                counter += 1
        if counter == self.tictactoe_board.size:
            return True

    def computermove(self, char):
        x = random.randint(0, self.tictactoe_board.size - 1)
        y = random.randint(0, self.tictactoe_board.size - 1)
        while self.tictactoe_board.getcell(x, y) != " ":
            x = random.randint(0, self.tictactoe_board.size - 1)
            y = random.randint(0, self.tictactoe_board.size - 1)
        self.tictactoe_board.placechar(x, y, char)

    def play(self):
        self.tictactoe_board.printboard()
        while True:
            x = readnum("Enter x coordinate from upper left: ")
            while x >= self.tictactoe_board.size:
                x = readnum("Invalid coordinate, enter number between 0 and " + str(len(self.tictactoe_board.size) - 1) + ": ")

            y = readnum("Enter y coordinate from upper left: ")
            while y >= self.tictactoe_board.size:
                y = readnum("Invalid coordinate, enter number between 0 and " + str(len(self.tictactoe_board.size) - 1) + ": ")

            if self.tictactoe_board.getcell(x, y) == " ":
                self.tictactoe_board.placechar(x, y, self.player)
                self.tictactoe_board.printboard()
                if self.checkboard(self.player):
                    self.result = "Player '" + self.player + "' won."
                    print(self.result)
                    break
                self.computermove(self.computer)
                print("Computer's move:")
                self.tictactoe_board.printboard()
                if self.checkboard(self.computer):
                    self.result = "Player '" + self.computer + "' won."
                    print(self.result)
                    break
            else:
                print("Can't place character here, cell is already occupied")

            decision = input("Would you like to continue playing? (y/n): ")
            if decision == "n":
                break


game = TicTacToeGame(readnum("Enter tictactoe board size: "), input("Enter player's character: "))
game.play()
