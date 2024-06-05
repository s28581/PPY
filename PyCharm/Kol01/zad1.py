import random

n = int(input('Enter a number: '))
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

diagonal_elements = list()
for i in range(len(matrix)):
    diagonal_elements.append(matrix[i][i])
    if i != len(matrix) - 1 - i:
        diagonal_elements.append(matrix[i][len(matrix) - 1 - i])

ranges = dict()
for i in range(10):
    ranges[(i*10, i*10+9)] = []

for row in matrix:
    for number in row:
        for key in ranges.keys():
            if key[0] < number < key[1]:
                ranges[key].append(number)

print("Matrix:")
for row in matrix:
    print(row)

print("\nElements on both diagonals:")
print(diagonal_elements)

print("\nElements in \"ranges\" dictionary:")
for item in ranges.items():
    print(item)
