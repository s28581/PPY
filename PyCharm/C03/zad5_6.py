k1 = (0, 1, 3)
k2 = (1, 2, 2)
k3 = (2, 3, 5)

l = [k1, k2, k3]

points = set()
for k in l:
    points.add(k[0])
    points.add(k[1])

matrix = []
for i in range(max(points)+1):
    row = []
    for j in range(max(points)+1):
        row.append(0)
    matrix.append(row)

for k in l:
    matrix[k[0]][k[1]] = k[2]

for row in matrix:
    print(row)

reverse = []
for row in range(len(matrix)):
    for i in range(len(matrix[row])):
        if matrix[row][i] != 0:
            k = (row, i, matrix[row][i])
            reverse.append(k)

print(reverse)
