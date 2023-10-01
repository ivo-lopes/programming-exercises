#mesmo exercício que o ex038, mas dessa vez o programa vai pedir novos números sempre que a entrada do usuário apresentar números iguais


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

def compara_n(n1, n2):
    return n1 == n2

while compara_n(n1, n2) is True:
    print('Os números são iguais. Tente novamente:')
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo valor ({n2}).')
else: 
    print(f'O segundo valor ({n2}) é maior que o primeiro valor ({n1}).')

input('Aperte ENTER para finalizar...')