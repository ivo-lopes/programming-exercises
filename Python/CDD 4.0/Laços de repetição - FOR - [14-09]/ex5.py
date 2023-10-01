n1 = int(input('Digite um valor inteiro positivo: '))
while n1 < 1:
    n1 = int(input('Valor inválido. Digite novamente: '))
n1 += 1
for x in range(1, n1):
    print(x)