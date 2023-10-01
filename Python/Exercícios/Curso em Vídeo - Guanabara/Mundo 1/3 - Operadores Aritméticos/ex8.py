# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Desafio pessoal: o programa deve perguntar em que medida o valor está sendo proposto e dar os valores correspondentes com as outras medidas mais populares

x = float(input('Digite um valor em metros: '))
cent = x*100
milim = x*1000
print(f'Esse valor corresponde a {cent} centímetros e {milim} milímetros.')