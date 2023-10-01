n = int(input('Digite a quantidade de elementos para a sequência de Fibonacci: '))
x = 0
y = 1
z = 0
cont = 1
print(f'')
while cont <= n:
    print(z)
    z = x + y
    y = x
    x = z
    cont += 1
    
