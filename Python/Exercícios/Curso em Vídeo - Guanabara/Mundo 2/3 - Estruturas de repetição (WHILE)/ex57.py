sexo = input('Digite M para masculino ou F para feminino: ')
while sexo not in 'MmFf':
    sexo = input('Entrada inválida! Tente novamente: ')
if sexo in 'Mm':
    print('masculino')
if sexo in 'Ff':
    print('feminino')