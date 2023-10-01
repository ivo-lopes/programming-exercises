ex1 = int(input('Digite o começo do intervalo de exercícios: '))
ex2 = int(input('Digite o final do intervalo de exercícios: '))
ex2 += 1
numero = 0
for numero in range(ex1, ex2):
    print(f'ex{numero}.py')
    with open(f'ex{numero}.py', 'x') as f:
        f.write('')
    numero += 1
    if numero == ex2:
        break
input('Arquivos criados! Aperte para continuar...')