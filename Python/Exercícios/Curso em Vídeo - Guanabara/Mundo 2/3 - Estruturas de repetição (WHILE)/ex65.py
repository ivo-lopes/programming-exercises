#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
n1 = 0
n2 = 0
cont = 0
cont1 = 1
maior = 0
menor = 0
while True:
    n2 = n1
    n1 = int(input('Digite um número: '))
    cont1 += 1
    cont += n1
    if n1 > n2:
        maior = n1
    if n1 < n2:
        menor = n1
    sair = input('Deseja encerrar o programa? (s/n) ')
    if sair not in 'SsNn':
        sair = input('Comando inválido. Deseja encerrar o programa? (s/n) ')
    if sair in 'Ss':
        break
    else:
        continue
print(maior)
print(menor)
print(cont)
