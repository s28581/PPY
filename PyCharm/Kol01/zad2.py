import random


def readnum(text):
    x = int(input(text))
    while x < 0 or x >= 20 or x % 2 != 0:
        x = int(input(text))
    return x


def createdict(x, values):
    d = dict()
    for i in range(x + 1):
        d[i] = random.choice(values)
    return d


def findmaxkey(dictionary, value):
    max_index = 0
    for key in dictionary.keys():
        if dictionary[key] == value and key > max_index:
            max_index = key
    return max_index


x1 = readnum("Enter x1: ")
x2 = readnum("Enter x2: ")
print("\nRead x1: " + str(x1))
print("Read x2: " + str(x2))

ab = createdict(x1, "ab")
print("\nDictionary ab:")
for item in ab.items():
    print(item)

cde = createdict(x2, "cde")
print("\nDictionary cde:")
for item in cde.items():
    print(item)

print("\nDictionary ab max key: " + str(findmaxkey(ab, "b")))
print("\nDictionary cde max key: " + str(findmaxkey(cde, "c")))
