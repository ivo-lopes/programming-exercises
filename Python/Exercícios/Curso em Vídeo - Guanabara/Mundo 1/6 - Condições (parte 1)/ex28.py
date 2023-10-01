from random import *
numero = randint(1, 5)
sorte = int(input('Digite um número de 1 a 5: '))
if numero == sorte:
    print(f'Parabéns, você acertou! O número era {numero}.')
else:
    print(f'Você errou! O número era {numero}.')