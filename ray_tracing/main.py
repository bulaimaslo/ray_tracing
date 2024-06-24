import sys
from vec3 import Vec3, unit_vector, dot
from color import write_color
from ray import Ray

def hit_sphere(center, radius, ray):
    oc = center - ray.origin
    a = dot(ray.direction, ray.direction)
    b = -2 * dot(ray.direction, oc)
    c = dot(oc, oc)  - radius**2
    discriminant = b*b - 4*a*c

    return discriminant >= 0

def ray_color(r: Ray):
    if hit_sphere(Vec3(0,0,-1), 0.5, r):
        return Vec3(1,0,0)

    # blendedValue=(1−a)*startValue+a*endValue where 0<=a<=1
    unit_direction = unit_vector(r.direction)
    a = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - a) * Vec3(1.0, 1.0, 1.0) + a * Vec3(0.5, 0.7, 1.0)
    # return Vec3(1.0, 1.0, 1.0)

def main():
    aspect_ratio = 16.0 / 9
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    camera_center = Vec3(0, 0, 0)

    viewport_u = Vec3(viewport_width, 0, 0)
    viewport_v = Vec3(0, viewport_height, 0)

    pixel_du = viewport_u * (1.0 / image_width)
    pixel_dv = viewport_v * (1.0 / image_height)

    viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 + viewport_v / 2
    pixel00_loc = viewport_upper_left + pixel_du / 2 - pixel_dv / 2

    sys.stdout.write(f"P3\n{image_width} {image_height}\n255\n")

    for j in range(image_height - 1, -1, -1):
        sys.stderr.write(f"\rScanlines remaining: {j} ")
        sys.stderr.flush()
        for i in range(image_width):
            pixel_center = pixel00_loc + pixel_du * i - pixel_dv * j
            ray_direction = pixel_center - camera_center
            ray = Ray(camera_center, ray_direction)
            pixel_color = ray_color(ray)
            write_color(sys.stdout, pixel_color)

    sys.stderr.write("\rDone.                 \n")

if __name__ == "__main__":
    main()

