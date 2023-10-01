import random
numeros = []


def sorteia():
    for x in range(5):
        numeros.append(random.randint(1, 20))
    print(numeros)


def somaPar(numeros):
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x
    return soma


sorteia()
print(f'A soma de todos os números PARES é: {somaPar(numeros)}')