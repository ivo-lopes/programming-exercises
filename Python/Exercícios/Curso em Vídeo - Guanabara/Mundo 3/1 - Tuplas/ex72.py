extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
innum = int(input('Digite um número de 0 a 10: '))
while innum not in range(11):
    innum = int(input('Valor inválido. Tente novamente: '))
print(extenso[innum])