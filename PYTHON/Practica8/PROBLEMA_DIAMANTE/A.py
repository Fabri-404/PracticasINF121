from C import C

class A(C):
    def __init__(self, x, z):
        C.__init__(self, z)
        self.x = x
    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1

