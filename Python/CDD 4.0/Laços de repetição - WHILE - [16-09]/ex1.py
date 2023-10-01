cont1 = 0
for x in range(10):
    valor = int(input('Digite um valor: '))
    if 10 <= valor <= 20:
        cont1 += 1
print(f'Dentro do intervalo de 10 a 20 estão {cont1} números.\nFora do intervalo de 10 a 20 estão {10-cont1} números.')