def readinput():
    try:
        return int(input("Enter integer <0,100>:"))
    except ValueError:
        print("Provided value was not integer, please enter integer")
        return readinput(

x = readinput()

while x > 100 or x < 0:
    print("Entered number did not meet requirements")
    x = readinput()
