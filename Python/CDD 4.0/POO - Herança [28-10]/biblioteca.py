class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        return self.valor


class Vip(Ingresso):
    def __init__(self, valorvip):
        super().__init__(valorvip)
        self.valor = valorvip.valor

    def imprimeVip(self):
        return self.valor * 1.5
