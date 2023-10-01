from random import randint
lista = []
maior = 0
for x in range(5):
    lista.append(randint(1, 20))
print()
menor = lista[0]
pos_menor = 0
for numeros in range(len(lista)):
    if lista[numeros] > maior:
        maior = lista[numeros]
        pos_maior = numeros
    if lista[numeros] < menor:
        menor = lista[numeros]
        pos_menor = numeros
    print(f'{numeros}. [{lista[numeros]}]')
print()
print(f'O maior número foi {maior} na posição {pos_maior}.')
print(f'O menor número foi {menor} na posição {pos_menor}.')
print()