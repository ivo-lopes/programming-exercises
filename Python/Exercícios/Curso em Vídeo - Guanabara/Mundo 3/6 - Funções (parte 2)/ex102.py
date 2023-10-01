def fatorial(num, show=False):
    fatorial = 1
    for x in range(num, 0, -1):
        fatorial = fatorial * x
        if show:
            print(x, end='')
            if x > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fatorial

teste = int(input('Digite um número: '))
mostrar = int(input('0 ou 1: '))
if mostrar == 1:
    mostrar = True
    print(f'{fatorial(teste, mostrar)}')
else:
    mostrar = False
    print(f'Fatorial: {fatorial(teste, mostrar)}')
