lista = []
cont = 0
cont_5 = 0

while True:
    n = int(input('Digite um número: '))
    if n == 5:
        cont_5 += 1
    lista.append(n)
    cont += 1
    continuar = input('Deseja continuar (s/n): ')
    if continuar in 'YySs':
        continue
    else:
        break

lista.sort()
lista.reverse()
print(lista)
print(f'Foram digitados {cont} número(s).')