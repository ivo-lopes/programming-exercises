print('Vamos construir um triângulo!')
lado1 = float(input('Digite o tamanho do lado 1: '))
lado2 = float(input('Digite o tamanho do lado 2: '))
lado3 = float(input('Digite o tamanho do lado 3: '))

if lado2 > lado1 and lado2 > lado3:
    hipotenusa = lado2
elif lado3 > lado1 and lado3 > lado2:
    hipotenusa = lado3
else: 
    hipotenusa = lado1

print(f'O maior lado mede {hipotenusa}. Este lado se chama Hipotenusa.')

if hipotenusa == lado1:
    somacateto = lado2 + lado3 
elif hipotenusa == lado2:
    somacateto = lado1 + lado3 
else:
    somacateto = lado1  + lado2 

print(f'A soma dos catetos ({somacateto}) deve ser maior que a hipotenusa ({hipotenusa}), logo:')

if somacateto > hipotenusa:
    print('Os lados PODEM formar um triângulo!')
else:
    print('Os lados NÃO podem formar um triângulo.')