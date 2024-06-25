from vec3 import Vec3
from sphere import Sphere
from hittable_list import HittableList
from camera import Camera

def main():
    world = HittableList()
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    cam = Camera(aspect_ratio=16.0 / 9.0, image_width=400, samples_per_px=100)
    cam.render(world)

if __name__ == "__main__":
    main()
