import math

class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def length(self):
        return math.sqrt(self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2)

    def __add__(self, other):
        return Vec3(self.e[0] + other.x(), self.e[1] + other.y(), self.e[2] + other.z())

    def __sub__(self, other):
        return Vec3(self.e[0] - other.x(), self.e[1] - other.y(), self.e[2] - other.z())

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.e[0] * t.x(), self.e[1] * t.y(), self.e[2] * t.z())
        return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)
    
    def __rmul__(self, t):
        return self * t

    def __truediv__(self, t):
        return self * (1/t)


def dot(v, t):
        return v.x() * t.x() + v.y() * t.y() + v.z() * t.z() 

def unit_vector(v):
    return v / v.length()

