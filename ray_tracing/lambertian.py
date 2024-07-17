from material import Material
from vec3 import random_unit_vector

class Lambertian(Material):
    def __init__(self, a):
        self.albedo = a # fraction of light absorbed

    def scatter(self, ray, rec, attenuation, scattered):
        scatter_direction = rec.normal + random_unit_vector()
        scattered.origin = rec.p
        scattered.direction = scatter_direction
        attenuation.e = self.albedo
        return True
