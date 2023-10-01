from bibliotecadeCLASSES import Pessoa

p1 = Pessoa('Ivo', 76, 19, 1.74)

print(f'{p1.nome} tem {p1.idade} anos, {p1.altura}m de altura e pesa {p1.peso}Kg.')
p1.menu()