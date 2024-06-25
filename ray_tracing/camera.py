import random
import sys
from vec3 import Vec3, unit_vector
from ray import Ray
from color import write_color
from interval import Interval
from hit_record import HitRecord

class Camera:
    def __init__(self, aspect_ratio=16.0 / 9.0, image_width=400, samples_per_px=10):
        self.aspect_ratio = aspect_ratio
        self.image_width = image_width
        self.image_height = max(1, int(self.image_width / self.aspect_ratio))
        self.center = Vec3(0, 0, 0)
        self.samples_per_px = samples_per_px
        self.initialize()

    def initialize(self):
        viewport_height = 2.0
        viewport_width = self.aspect_ratio * viewport_height
        focal_length = 1.0

        self.horizontal = Vec3(viewport_width, 0, 0)
        self.vertical = Vec3(0, viewport_height, 0)
        self.lower_left_corner = self.center - self.horizontal / 2 - self.vertical / 2 - Vec3(0, 0, focal_length)
        self.pixel_delta_u = self.horizontal / self.image_width
        self.pixel_delta_v = self.vertical / self.image_height
        self.pixel00_loc = self.lower_left_corner + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
        self.px_samples_scale = 1.0 / self.samples_per_px 
    
    def sample_square(self):
        return Vec3(random.random() - 0.5, random.random() - 0.5, 0)
    
    # Construct a camera ray originating from origing and directed at 
    #randomly sampled point around the px location i,j
    def get_ray(self, i, j):
        offset = self.sample_square()
        pixel_sample = self.pixel00_loc + ((i + offset.x()) * self.pixel_delta_u) + ((j + offset.y()) * self.pixel_delta_v)
        ray_origin = self.center
        ray_direction = pixel_sample - ray_origin
        
        return Ray(ray_origin, ray_direction)

    def ray_color(self, ray, world):
        rec = HitRecord()
        if world.hit(ray, Interval(0, float('inf')), rec):
            return 0.5 * (rec.normal + Vec3(1, 1, 1))
        unit_direction = unit_vector(ray.direction)
        t = 0.5 * (unit_direction.y() + 1.0)
        return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)

    def render(self, world):
        sys.stdout.write(f"P3\n{self.image_width} {self.image_height}\n255\n")

        for j in range(self.image_height - 1, -1, -1):
            sys.stderr.write(f"\rScanlines remaining: {j} ")
            sys.stderr.flush()
            for i in range(self.image_width):
                pixel_color = Vec3(0, 0, 0)
                for _ in range(self.samples_per_px):
                    ray = self.get_ray(i, j)
                    pixel_color +=  self.ray_color(ray, world)
                pixel_color *= self.px_samples_scale
                write_color(sys.stdout, pixel_color)

        sys.stderr.write("\rDone.                 \n")
