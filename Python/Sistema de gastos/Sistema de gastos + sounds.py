import pygame
pygame.init()

nome_usuario = ('ivonaldo')
senha_1 = ('ivonaldo123')

def compara_usuario(nome_usuario, usuario):
    return nome_usuario == usuario
def compara_senha(senha_1, senha):
    return senha_1 == senha

usuario = input('Usuário: ')
while compara_usuario(nome_usuario, usuario) is False:
    pygame.mixer.music.load('failure.wav')
    pygame.mixer.music.play()
    usuario = input('Usuário não encontrado. Digite novamente: ')
    pygame.mixer.music.load('sweep.wav')
    pygame.mixer.music.play()
    senha = input('Digite sua senha: ')
while compara_senha(senha_1, senha) is False:
    pygame.mixer.music.load('failure.wav')
    pygame.mixer.music.play()
    senha = input('Senha incorreta. Tente novamente: ')
    
pygame.mixer.music.load('notification.wav')
pygame.mixer.music.play()
print(f'Bem vindo, {usuario}!')
print('Acessando sistema de gastos...')
input('Aperte para continuar...')
pygame.mixer.music.load('sweep.wav')
pygame.mixer.music.play()



nome_mes = input('Especifique o mês que você gostaria de calcular seus gastos: ')
pygame.mixer.music.play()
saf = float(input('Digite o valor fixo do seu salário: '))
pygame.mixer.music.play()
g_f = float(input('Digite o valor dos seus gastos fixos: '))
pygame.mixer.music.play()
v_pc = float(input('Digite o valor da fatura do cartão de crédito: '))
pygame.mixer.music.play()
v_e = float(input('Digite o valor de renda extra: '))
pygame.mixer.music.play()
calculo_gast = (saf-g_f+v_e-v_pc)
gast = round(calculo_gast, 2)
pygame.mixer.music.load('drums.mp3')
pygame.mixer.music.play()
input('Calculando...')
if gast < 0:
    pygame.mixer.music.load('failure.wav')
    pygame.mixer.music.play()
else:
    pygame.mixer.music.load('coin.wav')
    pygame.mixer.music.play()
print(f'Em {nome_mes}, você terá saldo de:')
print(f'R${gast}')
exit = input('Aperte enter para finalizar...')
