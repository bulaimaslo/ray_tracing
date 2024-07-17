import math
from vec3 import dot
from hittable import Hittable
from hit_record import HitRecord

class Sphere(Hittable):
    def __init__(self, center, radius, mat):
        self.center = center
        self.radius = max(0, radius)
        self.mat = mat

    def hit(self, ray, ray_t, rec):
        if ray.origin is None or ray.direction is None:
            return False

        oc = ray.origin - self.center
        a = ray.direction.length() ** 2
        half_b = dot(oc, ray.direction)
        c = oc.length() ** 2 - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < ray_t.low or ray_t.high < root:
            root = (-half_b + sqrtd) / a
            if root < ray_t.low or ray_t.high < root:
                return False

        rec.t = root
        rec.p = ray.at(rec.t)
        rec.normal = (rec.p - self.center) / self.radius
        rec.mat = self.mat

        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(ray, outward_normal)
        
        return True

