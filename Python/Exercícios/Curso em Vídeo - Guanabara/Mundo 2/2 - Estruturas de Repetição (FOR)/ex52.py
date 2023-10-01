numero = int(input('Digite um número inteiro: '))
contador = 0
for x in range(1, numero+1):
    if numero % x == 0: 
        print(f'{numero} é divisível por {x}.')
        contador += 1
print(f'O número {numero} foi divisível {contador} vezes, logo...')
if contador == 2:
    print('Número PRIMO!')
else:
    print('Número NÃO PRIMO!')
