class Forma:
    def __init__(self, area=0, perimetro=0):
        self.area = area
        self.perimetro = perimetro

    def calculaArea(self):
        return self.area


class Retangulo(Forma):
    def __init__(self, base, altura, area=0, perimetro=0):
        super().__init__(area, perimetro)
        self.base = base
        self.altura = altura

    def calculaAreaRet(self):
        self.area = self.base * self.altura
        return self.area

    def calculaPerimetroRet(self):
        self.perimetro = (self.base * 2) + (self.altura * 2)
        return self.perimetro


class Triangulo(Forma):
    def __init__(self, base, altura, area=0, perimetro=0):
        super().__init__(area, perimetro)
        self.base = base
        self.altura = altura

    def calculaAreaTri(self):
        self.area = (self.base * self.altura) / 2
        return self.area

    def calculaPerimetroTri(self):
        self.perimetro = self.base * 3
        return self.perimetro
