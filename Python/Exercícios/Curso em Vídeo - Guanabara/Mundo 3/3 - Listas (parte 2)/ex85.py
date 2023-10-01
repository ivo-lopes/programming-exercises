from random import randint
lista = [[], []]

for x in range(7):
    temp = randint(1, 10)
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print(f'PARES: {lista[0]}')
print(f'IMPARES: {lista[1]}')
print(f'LISTA: {lista}')