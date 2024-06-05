import os
import random

# punkt a)
print("Punkt a)")
with open("test.txt", "r") as f:
    read_content = f.read()
    print(read_content)

# punkt b)
print("Punkt b)")
with open("test.txt", "r") as f:
    read_content = f.read()
    lines = read_content.splitlines()

with open('test2.txt.txt', 'w') as f:
    for line in lines:
        if len(line) > 5:
            f.write(line)

with open("test2.txt", "r") as f:
    read_content = f.read()
    print(read_content)

#punkt c)
print("\nPunkt c)")
lista = [[random.uniform(0,1) for i in range(10)] for j in range(10)]

with open('list.txt', 'w') as f:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            num = str(float(int(lista[i][j]*100))/100)
            if j == len(lista[i])-1:
                f.write(num)
            else:
                f.write(num + " ")
        if i != len(lista)-1:
            f.write("\n")

with open("list.txt", "r") as f:
    read_content = f.read()
    print(read_content)

# punkt d)
print("\nPunkt d)")
nums = list()
with open("list.txt", "r") as f:
    for num in f.readline().split(" "):
        nums.append(float(num))
print(nums)
