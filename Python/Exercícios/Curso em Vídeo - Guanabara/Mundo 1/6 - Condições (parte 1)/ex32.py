ano = int(input('Digite um ano: '))
bissexto = ano % 4 
if bissexto == 0:
    print('O ano é BISSEXTO')
else: 
    print('O ano NÃO é BISSEXTO')