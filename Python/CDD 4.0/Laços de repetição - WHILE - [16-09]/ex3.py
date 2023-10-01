alunos = int(input('Digite a quantidade de alunos para fazer a média aritmetica da sala: '))
cont = 0
cont1 = 0
while alunos > cont:
    nota = float(input('Digite um número: '))
    cont1 += nota
    cont += 1
media = cont1/alunos
print(f'A soma das notas foi {cont1}.\nA média da sala foi {media}.')