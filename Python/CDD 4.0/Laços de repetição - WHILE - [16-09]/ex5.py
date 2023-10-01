senha = 'ivonaldo123'
cont = 0
cont_tent = 2
senha1 = input('Digite a senha: ')
while senha1 != senha:
    senha1 = input(f'Senha incorreta. {cont_tent} tentativa(s) restante(s). Tente novamente: ')
    cont += 1
    cont_tent -= 1
    if cont == 2 or senha == senha1:
        break
if senha1 == senha:
    print('Senha correta. Acessando o sistema...')
    input('Aperte para continuar...')
else:
    print('Limite excedido. Usuário bloqueado.')