class Rectangulo:
    def __init__(self, punto_i, punto_f):
        self.punto_inicial = punto_i
        self.punto_final = punto_f
    def __init__(self, punto_i=(0, 0), punto_f=(0, 0)):
        self.punto_inicial = punto_i
        self.punto_final = punto_f
    def base(self):
        return abs(self.punto_final[0] - self.punto_inicial[0])
    def altura(self):
        return abs(self.punto_final[1] - self.punto_inicial[1])
    def area(self):
        return self.base() * self.altura()