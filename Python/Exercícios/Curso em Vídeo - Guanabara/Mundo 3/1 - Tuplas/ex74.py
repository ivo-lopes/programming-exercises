from random import *
lista = []
for x in range(5):
    lista.append(randint(0, 100))
maior = lista[0]
menor = lista[0]
print(lista)
for numero in range(5):
    if lista[numero] > maior:
        maior = lista[numero]
    if lista[numero] < menor:
        menor = lista[numero]
print(f'O maior número foi {maior}\nO menor número foi {menor}')
