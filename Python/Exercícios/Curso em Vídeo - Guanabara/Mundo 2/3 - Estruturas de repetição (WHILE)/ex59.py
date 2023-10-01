input('Bem vindo! Aperte para continuar...')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print()
while True:
    print(f'Números escolhidos: [{n1}] | [{n2}]:')
    action = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior valor\n[4] Inserir novos números\n[5] Sair do programa\n\nDigite: '))
    if action == 1:
        soma  = n1 + n2
        print(f'\n{n1} + {n2} = {soma}\n')
    if action == 2:
        produto  = n1 * n2
        print(f'\n{n1} * {n2} = {produto}\n')
    if action == 3:
        if n1 > n2:
            print(f'\n{n1} é maior que {n2}.\n')
        else:
            print(f'\n{n2} é maior que {n1}.\n')
    if action == 4:
        n1 = float(input('\nDigite um número: '))
        n2 = float(input('Digite outro número: '))
        print()
    if action == 5:
        input('\nFinalizando o programa...\nAperte para finalizar...')
        break