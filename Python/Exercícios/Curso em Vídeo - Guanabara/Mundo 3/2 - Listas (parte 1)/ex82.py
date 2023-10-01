from random import randint
lista1 = []
listaPAR = []
listaIMPAR = []

qntd = int(input('Quantos números deseja adicionar? '))
for x in range(qntd):
    lista1.append(randint(1, 30))
for numeros in range(len(lista1)):
    if lista1[numeros] % 2 == 0:
        listaPAR.append(lista1[numeros])
    else:
        listaIMPAR.append(lista1[numeros])

listaPAR.sort()
listaIMPAR.sort()

print('*'*(qntd*5))
print(f'Todos: {lista1}')
print(f'PARES: {listaPAR}')
print(f'ÍMPARES: {listaIMPAR}')
print('*'*(qntd*5))
