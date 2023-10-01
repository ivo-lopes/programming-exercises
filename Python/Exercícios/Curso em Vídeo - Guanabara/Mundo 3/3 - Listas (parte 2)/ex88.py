#AJUDE O JOGADOR DA MEGASENA
from random import randint
from time import sleep
jogos = []
temp = []

quantidade = int(input('Digite a quantidade de jogos que deseja criar: '))

for y in range(quantidade):
    for x in range(6):
        temp.append(randint(0, 60))
    jogos.append(temp[:])
    temp.clear()

print(f'+++++++++ < SORTEANDO {quantidade} JOGOS! > +++++++++')
for z in range(len(jogos)):
    print(f'Jogo {z+1}: {jogos[z]}')
    sleep(1)
print('+++++++++     < BOA SORTE! >     +++++++++')