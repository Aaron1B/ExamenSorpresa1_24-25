class punto ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.x is None:
            self.x = 0
        if self.y is None:
            self.y = 0
            def __str__(self):
                return f"({self.x},{self.y})"
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.y == 0 and self.x != 0:
            return "Eje X"
        else:
            return "Origen"
def vector(self, otro_punto):
    return (otro_punto.x - self.x, otro_punto.y - self.y)
