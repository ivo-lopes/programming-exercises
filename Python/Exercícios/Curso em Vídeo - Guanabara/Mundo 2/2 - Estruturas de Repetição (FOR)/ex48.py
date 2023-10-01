soma = 0
for impares in range(1, 500):
    if impares % 2 == 1:
        if impares % 3 == 0:
            soma += impares
print(soma)