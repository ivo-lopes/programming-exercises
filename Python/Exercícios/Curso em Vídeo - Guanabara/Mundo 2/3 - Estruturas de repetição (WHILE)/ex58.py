from random import *
sorte = randint(0, 10)
print(sorte)
cont = 3
numero = int(input('Adivinhe um número inteiro de 0 a 10: '))
while numero != sorte:
    if numero == sorte or cont == 1:
        cont -= 1
        break
    cont -= 1
    numero = int(input(f'Voce errou! {cont} tentativas restantes.\nDigite novamente um número de 0 a 10: '))
if cont == 0:
    print(f'Você atingiu o limite de tentativas. Você perdeu!')
else:
    print(f'Parabéns, você acertou!')
    
       