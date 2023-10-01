texto = input('Digite a expressão: ')
cont_parenteses_aberto = 0
cont_parenteses_fechado = 0
for caractere in range(len(texto)):
    if texto[caractere] == '(':
        cont_parenteses_aberto += 1
    if texto[caractere] == ')':
        cont_parenteses_fechado += 1
if cont_parenteses_aberto == 0 and cont_parenteses_fechado == 0:
    print('Sua expressão não possui parênteses!')
elif cont_parenteses_aberto != cont_parenteses_fechado:
    print('Expressão errada!')
else:
    print('Expressão correta!')
    