numero = int(input('Digite um número inteiro: '))
fatorial = 1
for x in range(numero, 1, -1):
    fatorial = fatorial * numero
    numero -= 1
print(fatorial) 