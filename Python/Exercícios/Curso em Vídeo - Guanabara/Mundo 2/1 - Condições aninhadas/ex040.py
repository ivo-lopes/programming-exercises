nota1 = float(input('Digite sua primeira nota: '))
while nota1 > 10 or nota1 <= 0:
    nota1 = float(input('Valor inválido. Digite sua primeira nota novamente: '))

nota2 = float(input('Digite sua segunda nota: '))
while nota2 > 10 or nota2 <= 0:
    nota2 = float(input('Valor inválido. Digite sua segunda nota novamente: '))

nota3 = float(input('Digite sua terceira nota: '))
while nota3 > 10 or nota3 <= 0:
    nota3 = float(input('Valor inválido. Digite sua terceira nota novamente: '))
       
media = (nota1 + nota2 + nota3)/3    

if media < 5:
    print(f'Sua média foi {media}: REPROVADO.')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media}: RECUPERAÇÃO.')
else:
    print(f'Sua média foi {media}: APROVADO.')