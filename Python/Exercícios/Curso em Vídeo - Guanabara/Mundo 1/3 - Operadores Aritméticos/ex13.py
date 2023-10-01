# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

x = float(input('Digite o valor do seu salário atual: '))
aumento = x+(x*0.15)
print(f'Seu salário de R${x}, foi reajustado para R${aumento}. Parabéns!')
