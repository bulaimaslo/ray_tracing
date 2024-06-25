from interval import Interval
from vec3 import Vec3

def write_color(out, pixel_color):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    intensity = Interval(0.0, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    out.write(f"{rbyte} {gbyte} {bbyte}\n")