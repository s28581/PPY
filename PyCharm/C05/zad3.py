import random

n = 5
matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
diagonal_elements = [transposed_matrix[i][i] for i in range(len(matrix))]

for row in matrix:
    print(row)

print()
for row in transposed_matrix:
    print(row)

print()
print(diagonal_elements)
