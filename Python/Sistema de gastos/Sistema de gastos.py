nome_usuario = ('ivonaldo')
senha_1 = ('ivonaldo123')

def compara_usuario(nome_usuario, usuario):
    return nome_usuario == usuario
def compara_senha(senha_1, senha):
    return senha_1 == senha

usuario = input('Usuário: ')
while compara_usuario(nome_usuario, usuario) is False:
    usuario = input('Usuário não encontrado. Digite novamente: ')
senha = input('Digite sua senha: ')
while compara_senha(senha_1, senha) is False:
    senha = input('Senha incorreta. Tente novamente: ')
    
print(f'Bem vindo, {usuario}!')
print('Acessando sistema de gastos...')
input('Aperte para continuar...')


nome_mes = input('Especifique o mês que você gostaria de calcular seus gastos: ')
saf = float(input('Digite o valor fixo do seu salário: '))
g_f = float(input('Digite o valor dos seus gastos fixos: '))
v_pc = float(input('Digite o valor da fatura do cartão de crédito: '))
v_e = float(input('Digite o valor de renda extra: '))
calculo_gast = (saf-g_f+v_e-v_pc)
gast = round(calculo_gast, 2)
input('Calculando...')
print(f'Em {nome_mes}, você terá saldo de:\nR${gast}')
exit = input('Aperte enter para finalizar...')
