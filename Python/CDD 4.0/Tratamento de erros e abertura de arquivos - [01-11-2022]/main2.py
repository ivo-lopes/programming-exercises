from datetime import datetime

while True:
    with open('arquivo.txt', 'a') as arquivo:
        hoje = datetime.now()
        data = hoje.strftime('%H:%M:%S - %d/%m/%Y')
        texto = input('>> ')
        if texto == '/exit':
            break
        arquivo.write(f'({data}) {texto} \n')


with open('arquivo.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)