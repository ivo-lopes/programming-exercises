lista = ['quilo', 'mouse', 'rato', 'roupa', 'queijo', 'carro', 'caralho', 'buceta', 'porta']
lista2 = []
for x in range(len(lista)):
    print(lista[x],end=': ')
    for letras in lista[x]:
        if letras in 'aeiou':
            print(letras, end='')
    print()