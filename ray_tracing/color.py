from interval import Interval
from vec3 import Vec3

def write_color(out, pixel_color):
    gamma_corrected = pixel_color.to_gamma()
    r = gamma_corrected.x()
    g = gamma_corrected.y()
    b = gamma_corrected.z()

    intensity = Interval(0.0, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    out.write(f"{rbyte} {gbyte} {bbyte}\n")