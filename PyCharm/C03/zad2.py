def readinput():
    try:
        return int(input("Enter integer:"))
    except ValueError:
        print("Provided value was not integer, please enter integer")
        return readinput()


x = readinput()
parzysta = x % 2 == 0
x = readinput()

while (x % 2 == 0) != parzysta:
    parzysta = x % 2 == 0
    x = readinput()
