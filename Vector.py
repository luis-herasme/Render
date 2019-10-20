import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def punto(self, otro):
        return otro.x * self.x + otro.y * self.y + otro.z * self.z

    def cruz(self, otro):
        return Vector(self.y*otro.z - self.z*otro.y, self.z*otro.x - self.x*otro.z, self.x*otro.y - self.y*otro.x)

    def cruzMag(self, otro):
        return math.sqrt((self.y*otro.z - self.z*otro.y)**2 + (self.z*otro.x - self.x*otro.z)**2 + (self.x*otro.y - self.y*otro.x)**2 )

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def sub(self, otro):
        return Vector(self.x-otro.x, self.y-otro.y, self.z-otro.z)

    def add(self, otro):
        return Vector(self.x+otro.x, self.y+otro.y, self.z+otro.z)

    def normalizar(self):
        mag = self.mag()
        self.x /= mag
        self.y /= mag
        self.z /= mag
