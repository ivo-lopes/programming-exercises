n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 == n2 : 
    print('Os números são iguais. Tente novamente.')
elif n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo valor ({n2}).')
else: 
    print(f'O segundo valor ({n2}) é maior que o primeiro ({n1}).')