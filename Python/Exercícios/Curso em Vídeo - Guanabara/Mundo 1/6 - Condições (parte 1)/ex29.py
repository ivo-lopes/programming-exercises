velocidade = float(input('Qual foi velocidade do veículo em Km/h? '))
multa = (velocidade - 80)*7
valor = round(multa, 2)
if velocidade >= 80:
     print(f'O veículo foi multado em R${valor}')
else:
    print('O veículo estava conforme a velocidade da via.')