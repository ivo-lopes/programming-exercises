while True:
    n1 = float(input('Digite a primeira nota: '))
    while n1 < 0 or n1 > 10:
        print('Nota inválida.')
        n1 = float(input('Digite novamente: '))
    n2 = float(input('Digite a segunda nota: '))
    while n2 < 0 or n2 > 10:
        print('Nota inválida.')
        n2 = float(input('Digite novamente: '))
    media = (n1+n2)/2
    print(f'Média: {media}')
    continuar = str(input('Deseja realizar novo cálculo? (y/n)  '))
    if continuar in 'Yy':
        continue
    elif continuar in 'Nn':
        input('Programa encerrado. Aperte enter para finalizar...')
        break
    else: 
        while continuar not in 'YyNn':
            continuar = str(input('Comando inválido!\nDeseja realizar novo cálculo? (y/n)  '))
