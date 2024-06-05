import random

tab = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(0,100))
    tab.append(row)

for i in range(len(tab)):
    print(tab[i])

maxvalues = []
localmax = 0

for i in range(len(tab[0])):
    for j in range(len(tab)):
        if tab[j][i] > localmax:
            localmax = tab[j][i]
    maxvalues.append(localmax)
    localmax = 0

print()
print(maxvalues)
