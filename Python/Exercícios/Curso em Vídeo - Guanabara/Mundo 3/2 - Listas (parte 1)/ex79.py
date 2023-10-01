from random import randint
lista = []
duplicados = []
for x in range(5):
    numero = randint(1, 10)
    if numero in lista:
        print('Valor duplicado!')
        duplicados.append(numero)
    else:
        lista.append(numero)
print(lista)
print(duplicados)