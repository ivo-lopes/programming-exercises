import ex99functions
numeros = []
cont = 1

while True:
    temp = input(f'{cont}. Digite um número (quit to stop): ')
    if temp == 'quit':
        break
    cont+=1
    numeros.append(float(temp))

print(numeros)
maior = ex99functions.maior(numeros)
print(maior)