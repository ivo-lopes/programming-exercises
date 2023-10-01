from time import *
def contador(x, y, z):
    for primeiro in range(1, 11):
        print(primeiro, end=' ', flush=True)
        sleep(0.2)
    print()
    for segundo in range(10, -2, -2):
        print(segundo, end=' ', flush=True)
        sleep(0.2)
    print()
    for terceiro in range(x, y, z):
        print(terceiro, end=' ', flush=True)
        sleep(0.2)
    print()

começo = int(input('Digite o começo do intervalo: '))
final = int(input('Digite o final do intervalo: '))
pace = int(input('Digite o passo do intervalo: '))
if final/começo < 1:
    pace = pace*-1
contador(começo, final, pace)