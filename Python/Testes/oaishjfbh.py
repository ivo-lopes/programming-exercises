lista = []
cont = 1
while True:
    lista.append(input(f'{cont}. Digite um item: '))
    confirm = input('Deseja adicionar outro item? (s/n): ')
    if confirm in 'yYsS':
        cont+=1
        continue
    elif confirm in 'Nn':
        break


def contador(lista):
    cont_cont = 0
    for x in lista:
        cont_cont+=1
    print(lista)
    print(cont_cont)


contador(lista)