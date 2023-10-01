n1 = int(input('Digite o começo do intervalo: '))
n2 = int(input('Digite o final do intervalo: '))
n2 += 1
numeros_pares = 0
numeros_impares = 0

print('Números PARES:')
for x in range(n1, n2):
    if x % 2 == 0:
        numeros_pares += 1
        print(x)
print('Números ÍMPARES:')
for x in range(n1, n2):
    if x % 2 != 0:
        numeros_impares += 1
        print(x)
input('Aperte para continuar...')
print(f'NÚMEROS PARES: {numeros_pares}')
print(f'NÚMEROS ÍMPARES: {numeros_impares}')
