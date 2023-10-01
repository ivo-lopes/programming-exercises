teclado = input('Qual o modelo do seu teclado?')
esta_limpo = input('Há quantos dias você não limpa seu teclado?')
if esta_limpo < 60:
    print ('Parabéns! Seu' , teclado , 'está limpo!')
if esta_limpo > 60:
    print ('Puta que pariu, né... vá limpar seu' , teclado +  '! Fazem' , esta_limpo , 'dias que voçê não o limpa!')
