from functions import *

alunos = []
medias = []

for x in range(3):
    aluno = input('Aluno: ')
    nota1 = float(input('Nota 1: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Valor inválido. Nota 1: '))
    nota2 = float(input('Nota 2: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Valor inválido. Nota 2: '))
    calc_media(aluno, nota1, nota2)

print(alunos)
print(medias)
