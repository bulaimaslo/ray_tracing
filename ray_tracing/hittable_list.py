from hittable import Hittable
from hit_record import HitRecord
from interval import Interval

class HittableList(Hittable):
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def hit(self, ray, ray_t, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_t.high

        for obj in self.objects:
            if obj.hit(ray,  Interval(ray_t.low, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal

        return hit_anything
