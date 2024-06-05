import random

l = []
for i in range(10):
    l.append(random.randint(0, 100))
print(l)

m = None
for i in l:
    if i % 2 == 0:
        m = i
        break

for i in l:
    if (i % 2 == 0) and i < m:
        m = i

print(m)
