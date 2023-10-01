class Atleta:
    def __init__(self, peso, aposentado=False, aquecido=False):
        self.aquecido = aquecido
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print('Se aposentou.')

    def aquecer(self):
        self.aquecido = True
        print('Aqueceu.')


class Corredor(Atleta):
    def __init__(self, peso, aposentado, correndo):
        super().__init__(peso, aposentado)
        self.correndo = correndo

    def correr(self):
        if not self.aposentado:
            if not self.aquecido:
                print('Não está aquecido!')
            else:
                if self.correndo == True:
                    print('Já está correndo.')
                else:
                    self.correndo = True
                    print('Está correndo.')
        else:
            print('Está aposentado, não pode correr.')
    
    def parar_correr(self):
        self.correndo = False
        print('Parou de correr.')


class Nadador(Atleta):
    def __init__(self, peso, aposentado, nadando):
        super().__init__(peso, aposentado)
        self.nadando = nadando

    def nadar(self):
        if not self.aposentado:
            if not self.aquecido:
                print('Não está aquecido!')
            else:
                if self.nadando == True:
                    print('Já está nadando.')
                else:
                    self.nadando = True
                    print('Está nadando.')

        else:
            print('Está aposentado, não pode nadar.')

    def parar_nadar(self):
        self.nadando = False
        print('Parou de nadar.')

class Ciclista(Atleta):
    def __init__(self, peso, aposentado, pedalando):
        super().__init__(peso, aposentado)
        self.pedalando = pedalando

    def pedalar(self):
        if not self.aposentado:
            if not self.aquecido:
                print('Não está aquecido!')
            else:
                if self.pedalando == True:
                    print('Já está pedalando.')
                else:
                    self.pedalando = True
                    print('Está pedalando.')
        else:
            print('Está aposentado, não pode pedalar.')
    
    def parar_pedalar(self):
        self.pedalando = False
        print('Parou de pedalar.')


class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, pedalando=False, correndo=False, nadando=False):
        super().__init__(pedalando, correndo, nadando)
