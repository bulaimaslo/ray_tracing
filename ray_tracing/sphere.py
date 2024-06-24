import math
from vec3 import Vec3, dot
from hittable import Hittable
from hit_record import HitRecord
from ray import Ray

class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = max(0, radius)

    def hit(self, ray, t_min, t_max, rec):
        oc = ray.origin - self.center
        a = ray.direction.length() ** 2
        half_b = dot(oc, ray.direction)
        c = oc.length() ** 2 - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        #Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = ray.at(rec.t)
        rec.normal_v = (rec.p - self.center) / self.radius

        return True
