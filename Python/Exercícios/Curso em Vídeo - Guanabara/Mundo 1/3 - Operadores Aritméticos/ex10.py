# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere U$1.00 = R$5.54

x = float(input('Digite um valor em reais para ser convertido em dólares: '))
y = x/5.54
reais = round(x, 2)
dolares = round(y, 2)
print(f'Em conversão direta, R${reais} equivalem a U${dolares}.')