n1 = int(input('Digite o primeiro número: '))
while n1 == 0 or n1 < 0:
    print('Digite um número diferente de 0 e positivo.')
    n1 = int(input('Digite novamente o primeiro número: '))

n2 = int(input('Digite o segundo número: '))
while n2 == 0 or n2 < 0:
    print('Digite um número diferente de 0 e positivo.')
    n2 = int(input('Digite novamente o segundo número: '))

divisao = n1/n2
print(f'{n1} / {n2} =', divisao)