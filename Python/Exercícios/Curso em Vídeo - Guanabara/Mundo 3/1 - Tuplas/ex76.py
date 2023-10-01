lista = []
soma = 0
cont = 1
def linha(simbolo):
    print(simbolo*50)
while True:
    lista.append(input(f'{cont}. Digite o produto: '))
    lista.append(float(input(f'{cont}. Digite o preço: ')))
    continuar = input('Deseja adicionar outro produto? (s/n): ')
    if continuar in 'yyYYssSS':
        cont+=1
        continue
    if continuar in 'nnNN':
        break
print(lista)
linha('=')
print(f'{"Lista de Compras":^50}')
linha('=')
for produtos in range(len(lista)):
    if produtos % 2 == 0:
        print(f'{lista[produtos]:.<40}', end='')
    else:
        soma += lista[produtos]
        print(f'R$ {float(lista[produtos]):>7.2f}')
linha('-')
print(f'{"Total:":.<40}', end='')
print(f'R$ {soma :>7.2f}')
linha('=')