numero = int(input('Digite um número: '))
fator = 0
for x in range(0, 11):
    print(f'{numero} * {fator} =', numero*fator)
    fator += 1