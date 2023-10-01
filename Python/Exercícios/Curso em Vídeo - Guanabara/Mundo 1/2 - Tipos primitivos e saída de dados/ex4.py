# Proposta: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Meu objetivo: fazer o programa identificar se o input é numérico ou alfabético e dar apenas uma resposta sobre isso.


x = input('Digite algo:')
alpha = x.isalpha
numeric = x.isnumeric

if alpha: True
print(f'{x} é formado apenas por letras!')

if numeric: True
print(f'{x} é um número!')