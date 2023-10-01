numeros = []
cont = 1


def maior(numeros):
    maior = 0
    for x in numeros:
        if x > maior:
            maior = x
    return maior


while True:
    temp = input(f'{cont}. Digite um número (quit to stop): ')
    if temp == 'quit':
        break
    cont+=1
    numeros.append(float(temp))

print(numeros)
maior = maior(numeros)
print(maior)