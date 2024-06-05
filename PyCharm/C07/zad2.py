n = int(input("Enter size: "))
board = [[" " for _ in range(n)] for _ in range(n)]
for row in board:
    print(row)


class BoardBoundaryException(Exception):
    def __init__(self, value, size):
        self.value = value
        self.size = size
        message = "Value {} is out of bounds for board size {}".format(value, size)
        super().__init__(message)


x = int
y = int
try:
    while True:
        x = int(input("Enter x: "))
        if x > n-1 or x < 0:
            raise BoardBoundaryException(x, n)
        y = int(input("Enter y: "))
        if y > n-1 or y < 0:
            raise BoardBoundaryException(y, n)
except ValueError:
    print("Input value was not an integer - aborting.")
