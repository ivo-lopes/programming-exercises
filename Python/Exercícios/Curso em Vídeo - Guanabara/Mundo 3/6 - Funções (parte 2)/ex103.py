def desempenho(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


jogador = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    desempenho(gols=gols)
else:
    desempenho(jogador, gols)