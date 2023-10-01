from datetime import datetime

def menu():
    while True:
        hoje = datetime.now()
        data = hoje.strftime('%H:%M:%S - %d/%m/%Y')
        print(f'===================================\n'
              f'1. Soma\n'
              f'2. Subtração\n'
              f'3. Multiplicação\n'
              f'4. Divisão\n'
              f'5. Sair (encerrar programa)\n'
              f'===================================')
        action = int(input('Ação: '))
        while action not in range(1, 6):
            action = int(input('Comando inválido. Tente novamente: '))
        if action == 5:
            input(f'{data} --> Programa encerrado.\n'
                  f'Aperte ENTER para continuar...\n')         
            break
        n1 = float(input('1º número: '))
        n2 = float(input('2º número: '))
        if action == 1:
            print(f'{data} --> {soma(n1, n2)}')
            continue
        elif action == 2:
            print(f'{data} --> {subtracao(n1, n2)}')
            continue
        elif action == 3:
            print(f'{data} --> {multiplicacao(n1, n2)}')
            continue
        elif action == 4:
            print(f'{data} --> {divisao(n1, n2)}')
            continue
            


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    try:
        return n1 / n2

    except ZeroDivisionError as erro:
        print(f'Ops... Ocorreu um erro! --> {erro}')
