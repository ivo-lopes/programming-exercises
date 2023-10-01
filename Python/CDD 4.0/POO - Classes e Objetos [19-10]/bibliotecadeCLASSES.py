class Pessoa:
    def __init__(self, nome, peso, idade, altura, comendo=False, dormindo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.altura = altura
        self.dormindo = dormindo
        self.falando = falando

    # COMANDOS PARA INICIAR AÇÕES

    def comer(self):
        if self.falando == True:
            print(f'{self.nome} não pode comer porque ele está falando.')
        else:
            if self.dormindo == True:
                print(f'{self.nome} não pode comer porque ele está dormindo.')
            else:
                if self.comendo == False:
                    self.comendo = True
                    print(f'{self.nome} foi comer.')
                else:
                    print(f'{self.nome} já está comendo.')

    def dormir(self):
        if self.falando == True:
            print(f'{self.nome} não pode dormir porque ele está falando.')
        else:
            if self.comendo == True:
                print(f'{self.nome} não pode dormir porque ele está comendo.')
            else:
                if self.dormindo == False:
                    self.dormindo = True
                    print(f'{self.nome} foi dormir.')
                else:
                    print(f'{self.nome} já está dormindo.')

    def falar(self):
        if self.dormindo == True:
            print(f'{self.nome} não pode falar porque ele está dormindo.')
        else:
            if self.comendo == True:
                print(f'{self.nome} não pode falar porque ele está comendo.')
            else:
                if self.falando == False:
                    self.falando = True
                    print(f'{self.nome} está falando.')
                else:
                    print(f'{self.nome} já está comendo.')

    # COMANDOS PARA FINALIZAR AÇÕES:

    def stopComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f'{self.nome} parou de comer.')
        else:
            print(f'{self.nome} não pode parar de comer porque ele não está comendo.')

    def stopDormir(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f'{self.nome} acordou.')
        else:
            print(f'{self.nome} não pode acordar porque ele não está dormindo.')

    def stopFalar(self):
        if self.falando == True:
            self.falando = False
            print(f'{self.nome} Parou de falar.')
        else:
            print(f'{self.nome} não pode parar de falar porque ele não está falando.')

    #############


    def menu(self):
        while True:
            if self.comendo == True:
                print(f'{self.nome} está comendo.')
            if self.dormindo == True:
                print(f'{self.nome} está dormindo.')
            if self.falando == True:
                print(f'{self.nome} está falando.')
            print('*'*30)
            print('1. Dormir')
            print('2. Comer')
            print('3. Falar')
            print('4. Parar de dormir')
            print('5. Parar de comer')
            print('6. Parar de falar')
            print('*' * 30)
            action = int(input('Digite uma ação (7 para encerrar): '))
            if action == 1:
                self.dormir()
            if action == 2:
                self.comer()
            if action == 3:
                self.falar()
            if action == 4:
                self.stopDormir()
            if action == 5:
                self.stopComer()
            if action == 6:
                self.stopFalar()
            if action == 7:
                break

