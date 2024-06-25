import sys
from vec3 import Vec3, unit_vector
from ray import Ray
from color import write_color
from sphere import Sphere
from hittable_list import HittableList
from hit_record import HitRecord
from interval import Interval

def ray_color(ray, world):
    rec = HitRecord()
    if world.hit(ray, Interval(0.001, float('inf')), rec):
        return 0.5 * (rec.normal + Vec3(1, 1, 1))
    unit_direction = unit_vector(ray.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)

def main():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    image_height = max(1, image_height)

    # World
    world = HittableList()
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Vec3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

    sys.stdout.write(f"P3\n{image_width} {image_height}\n255\n")

    for j in range(image_height - 1, -1, -1):
        sys.stderr.write(f"\rScanlines remaining: {j} ")
        sys.stderr.flush()
        for i in range(image_width):
            u = i / (image_width - 1)
            v = j / (image_height - 1)
            direction = lower_left_corner + u*horizontal + v*vertical - origin
            ray = Ray(origin, direction)
            pixel_color = ray_color(ray, world)
            write_color(sys.stdout, pixel_color)

    sys.stderr.write("\rDone.                 \n")

if __name__ == "__main__":
    main()
