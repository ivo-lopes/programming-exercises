num0 = [12,43,34,76,123,45,98,23,678]
num12 = [1,2,3,4,5,6,7,8,9,10]
num = []
for numeros in range(5):
    num.append(int(input('Insira um número na lista: ')))
print(num)


def dobrar(lista):
    for x in range(len(lista)):
        lista[x] = lista[x]*2
    print(lista)

dobrar(num)
dobrar(num0)
dobrar(num12)