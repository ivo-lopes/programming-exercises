lista = []
pessoas = []
cont = 1
maior = 0
menor = 0

while True:
    pessoas.append(input(f'{cont}. Digite o nome da pessoa: '))
    pessoas.append(float(input(f'{cont}. Digite o peso da pessoa: '))) 
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    continuar = input('Deseja continuar? (s/n): ')
    if continuar in 'YySs':
        cont += 1
        continue
    else:
        cont = 1
        break

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg e o menor foi de {menor}Kg.')
