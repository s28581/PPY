import random

print("Zadanie 1\n")
array = list(range(0, 101, 5))
print(array[::-1])
print(array[4::-2])
print(array[0:(int(len(array) / 2))])

sum = 0
for i in range(int(len(array) / 2)):
    print(str(array[i]) + " ", end='')
    sum += array[i]
print()

print(sum / len(array))
array.remove(90)
print(array)
temp = array[0]
array[0] = array[-1]
array[-1] = temp
print(array)
tup = tuple(array)
second = tup[1]
last = tup[-1]
print("Tuple: " + str(tup))
print("Second elem: " + str(second) + ", last: " + str(last))
print("----------------------------------------")
print("Zadanie 2\n")
l1 = list()
l2 = list()
for i in range(5):
    l1.append(random.randint(0, 10))
for i in range(10):
    l2.append(random.randint(0, 10))
print("List 1:" + str(l1))
print("List 2:" + str(l2))
unique_sum = set(l1 + l2)
print("Joined elements: " + str(unique_sum))
set1 = set(l1)
set2 = set(l2)
print("List 2 elements without list 1 elements: " + str(set2.difference(set1)))
print("----------------------------------------")
print("Zadanie 3\n")
l3 = list()
for i in range(100):
    l3.append(random.randint(0, 10))
print("List:" + str(l3))
d = {}
for i in range(11):
    d[i] = l3.count(i)
print(d)
print("----------------------------------------")
print("Zadanie 4\n")
ceny = {"jablka": 2.5, "czekolada": 10}
print(ceny)
lista_zakupow = {}
print(lista_zakupow)
#produkt = input("Produkt: ")
#ilosc = float(input("Ilość: "))
#lista_zakupow[produkt] = ilosc
#print(lista_zakupow)
#suma = 0
#for p in lista_zakupow.keys():
#    suma += lista_zakupow[p] * ceny.get(p, 0)
#print("Suma: " + str(suma))
print("----------------------------------------")
print("Zadanie 5\n")
k1 = {"autor": "Haruki Murakami", "tytul": "Kafka nad morzem", "year": 2002, }
k2 = {"autor": "Atwood", "tytul": "Służąca opowieść", "year": 2019, }
k3 = {"autor": "Atwood", "tytul": "Norweski las", "year": 1987, }
d3 = [k1, k2, k3]
print(d3[1].get("autor"))
for i in range(len(d3)):
    if d3[i].get("autor") == "Atwood":
        print(d3[i])
