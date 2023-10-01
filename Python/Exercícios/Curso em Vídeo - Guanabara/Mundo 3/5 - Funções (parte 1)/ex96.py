from random import *
def area(x, y):
    area = x*y
    print(f'Área: {area}m².')

comprimento = randint(10, 50)
print(comprimento)
largura = randint(10, 50)
print(largura)
area(comprimento, largura)