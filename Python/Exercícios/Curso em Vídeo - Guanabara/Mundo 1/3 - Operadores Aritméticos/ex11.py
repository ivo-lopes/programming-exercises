# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la;
# Sabe-se que cada litro de tinta pinta uma área de 2**2m

x = float(input('Digite a altura da parede em metros: '))
y = float(input('Digite a largura da parede em metros: '))
area = x*y
tinta = area/2
print(f'Você precisará de {tinta} litros de tinta para fazer essa pintura.')