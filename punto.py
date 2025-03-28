class punto ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.x is None:
            self.x = 0
        if self.y is None:
            self.y = 0