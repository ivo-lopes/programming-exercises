num = input('Digite um número: ')
def leiaInt(num):
    if num.isnumeric():
        num = int(num)
    else:
        while True:
            num = input('Digite um número: ')
            