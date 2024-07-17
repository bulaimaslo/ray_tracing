from vec3 import Vec3
from sphere import Sphere
from hittable_list import HittableList
from camera import Camera
from lambertian import Lambertian
from metal import Metal

def main():
    world = HittableList()

    material_ground = Lambertian(Vec3(0.8, 0.8, 0.0))
    material_center = Lambertian(Vec3(0.7, 0.3, 0.3))
    material_left = Metal(Vec3(0.8, 0.8, 0.8))
    material_right = Metal(Vec3(0.8, 0.6, 0.2))

    world.add(Sphere(Vec3(0, -100.5, -1), 100, material_ground))
    world.add(Sphere(Vec3(0, 0, -1), 0.5, material_center))
    world.add(Sphere(Vec3(-1, 0, -1), 0.5, material_left))
    world.add(Sphere(Vec3(1, 0, -1), 0.5, material_right))

    cam = Camera(aspect_ratio=16.0 / 9.0, image_width=400, samples_per_px=100)
    cam.render(world)

if __name__ == "__main__":
    main()
