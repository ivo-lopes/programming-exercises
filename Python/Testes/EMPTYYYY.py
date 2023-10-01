cont = 1

def func():
    global cont
    for i in (1, 2, 3):
        cont += 1


for x in range(2, 30, 3):
    cont +=1

print(cont)