def readinput():
    try:
        return int(input("Enter height: "))
    except ValueError:
        print("Provided value was not integer, please enter integer")
        return readinput()


height = readinput()
width = height*2-1
half = int(width/2)
char = input("Enter char: ")

for i in range(height):
    print(" "*half + char*(width-2*half) + " "*half)
    half -= 1
