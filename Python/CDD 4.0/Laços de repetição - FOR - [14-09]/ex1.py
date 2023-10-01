nome = input('Digite seu nome: ')
numero = 0
for x in nome:
    print(x)
    if x != ' ':
        numero += 1
print(f'{nome} tem {numero} letras.')