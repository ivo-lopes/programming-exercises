viagem = float(input('Informe a distância da sua viagem (em Km/h): '))
if viagem > 200:
    preco = viagem * 0.45
    print(f'A sua viagem é de longa duração. Custará R${preco}')
else:
    preco = viagem * 0.5
    print(f'A sua viagem é de curta duração. Custará R${preco}')