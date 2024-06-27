import random
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

    def length_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2

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
    
    def to_gamma(self):
        return Vec3(
            math.sqrt(max(self.x(), 0)),
            math.sqrt(max(self.y(), 0)),
            math.sqrt(max(self.z(), 0))
        )

    def unit_vector(self):
        return self / self.length()
    
    @staticmethod
    def random(min=0.0, max=1.0):
        return Vec3(random.uniform(min, max), random.uniform(min, max), random.uniform(min, max))

    @staticmethod
    def random_in_unit_sphere():
        while True:
            p = Vec3.random(-1, 1)
            if p.length_squared() < 1:
                return p
    
    @staticmethod
    def random_unit_vector():
        return Vec3.random_in_unit_sphere().unit_vector()
    
    @staticmethod
    def random_on_hemisphere(normal):
        in_unit_sphere = Vec3.random_unit_vector()
        if dot(in_unit_sphere, normal) > 0:
            return in_unit_sphere
        else:
            return in_unit_sphere * -1

def dot(v, t):
    return v.x() * t.x() + v.y() * t.y() + v.z() * t.z() 

def unit_vector(v):
    return v / v.length()

def clamp(x, min_val, max_val):
    return max(min_val, min(x, max_val))