from vec3 import dot

class HitRecord:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = 0
        self.front_face = False

    def set_face_normal(self, ray, outward_normal):
        self.front_face = dot(ray.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -1 * outward_normal