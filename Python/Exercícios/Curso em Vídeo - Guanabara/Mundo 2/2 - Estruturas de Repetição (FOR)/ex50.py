soma = 0
for x in range(0, 6):
    pares = int(input('Digite um número: '))
    if pares % 2 == 0:
        soma += pares
print(f' A soma de todos os números pares digitados foi: {soma}')
