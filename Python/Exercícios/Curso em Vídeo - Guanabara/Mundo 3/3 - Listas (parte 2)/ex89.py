lista = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    for x in range(2):
        notas.append(float(input(f'Nota {x+1}: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = input('Deseja continuar? [s/n]: ')
    if continuar in 'YySs':
        continue
    else:
        print(lista)
        for x in range(len(lista)):
            media = (lista[x][1][0] + lista[x][1][1])/2 
            print(f'{x+1}. {lista[x][0]}   |   Média: {media}')
        input('Programa encerrado. Aperte ENTER para continuar...')
        break
    
