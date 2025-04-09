from A import A
from B import B

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x)
        B.__init__(self, y)
        self.z = z
    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"