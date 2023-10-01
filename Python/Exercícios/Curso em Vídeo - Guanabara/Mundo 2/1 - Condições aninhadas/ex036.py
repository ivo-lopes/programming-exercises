casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos você vai pagar: '))
prestacao_mensal = casa / (anos * 12)
parcela_salario = prestacao_mensal / salario * 100
print(f'Prestação mensal: R${round(prestacao_mensal, 2)} ({round(parcela_salario, 2)}%)')

if prestacao_mensal > salario * 0.3 :
    print('Empréstimo NEGADO')
else: 
    print('Empréstimo APROVADO')
