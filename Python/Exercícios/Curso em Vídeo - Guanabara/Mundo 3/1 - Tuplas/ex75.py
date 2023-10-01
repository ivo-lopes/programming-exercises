from random import *
n = []
cont9 = 0
pos3 = []
par = []
for x in range(10):
    n.append(randint(1, 10))
print(n)
for x in range(10):
    if n[x] == 9:
        cont9 += 1
    if n[x] == 3:
        pos3.append(x)
    if n[x] % 2 == 0:
        par.append(n[x])
print   (f'O número 9 apareceu {cont9} vez(es).\n'
         f'O número 3 apareceu nas seguintes posições: {pos3}\n'
         f'Estes foram os números pares: {par}')