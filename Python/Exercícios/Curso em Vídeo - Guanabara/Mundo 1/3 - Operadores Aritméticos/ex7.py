# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
# Desafio pessoal: colocar uma condição para que o aluno seja aprovado a partir de uma determinada média
 
print('Nota: para que o aluno seja aprovado, a média das notas de suas recuperações deve ser superior a 7.')
print('Para continuar, tecle Enter...')
nome = input('Qual o nome do(a) aluno(a)? ')
x = float(input('Qual foi o resultado da primeira prova? '))
y = float(input('Qual foi o resultado da segunda prova? '))
media = (x+y)/2

if media>=7:
    print(f'Parabéns, {nome} está aprovado! A média de suas notas foi {media}')
else:
    print(f'Infelizmente {nome} não foi aprovado(a), sua média foi {media}.')
