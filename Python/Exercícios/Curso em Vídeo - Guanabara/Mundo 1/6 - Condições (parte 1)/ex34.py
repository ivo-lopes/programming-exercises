salario = float(input('Digite seu salário atual: '))
if salario <= 1250:
    aumento = salario * 1.15
    print(f'Seu aumento foi de 15%. Seu novo salário é de R${aumento}.')
else:
    aumento = salario * 1.1
    print(f'Seu aumento foi de 10%. Seu novo salário é de R${aumento}')