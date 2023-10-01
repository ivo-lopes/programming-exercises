import random
def sorteia(numeros):
    for x in range(5):
        numeros.append(random.randint(1, 20))
    print(numeros)


def somaPar(numeros):
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x
    return soma
