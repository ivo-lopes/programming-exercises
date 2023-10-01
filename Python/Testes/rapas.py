maca = 1.3
quantidade = int(input('Digite a quantidade de maçãs que desejas comprar: '))
if quantidade >= 12:
    maca = 1
custo = quantidade * maca
print(f'Você comprou {quantidade} maçãs.\n'
      f'Custou R${round(custo, 2)}')