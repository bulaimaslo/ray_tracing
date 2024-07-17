from material import Material
from vec3 import random_unit_vector, dot
from ray import Ray

class Metal(Material):
    def __init__(self, a):
        self.albedo = a # fraction of light absorbed

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = r_in.direction.unit_vector().reflect(rec.normal)
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo

        return True
