aulas = int(input('Digite a quantidade de aulas que você deseja criar: '))
numero = 0
for numero in range(0,100):
    print(f'ex{numero}.py')
    numero = numero + 1
    if numero == aulas:
        break
print('FIM')