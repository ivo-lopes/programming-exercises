negativo = 0
for x in range(9):
    n1 = int(input('Digite um valor: '))
    if n1 < 0:
        negativo += 1
print(f'NEGATIVOS: {negativo}')