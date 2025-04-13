from C import C

class B(C):
    def __init__(self, y, z):
        C.__init__(self, z)

        self.y = y
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1