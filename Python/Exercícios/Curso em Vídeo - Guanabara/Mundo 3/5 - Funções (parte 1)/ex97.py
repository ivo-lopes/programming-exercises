from time import *


def escreva(string):
    print(f'{"~"*40}')
    print(f'{string:^40}')
    print(f'{"~"*40}')


text = input('Escreva qualquer coisa: ')

escreva(text)
