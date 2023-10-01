n1 = int(input('Digite um número: '))
cont = 1
soma = n1
while True:
    n1 = int(input('Digite outro número (ou digite 999 para sair): '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
    
print(f'Foram digitados {cont} números. A somatória é {soma}.')