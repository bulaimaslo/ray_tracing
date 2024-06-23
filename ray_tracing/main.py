import sys
from vec3 import Vec3
from color import write_color

def main():
    image_width = 256
    image_height = 256

    sys.stdout.write(f"P3\n{image_width} {image_height}\n255\n")

    for i in range(image_height):
        sys.stderr.write(f"\rScanlines remaining: {image_height - i} ")
        sys.stderr.flush()
        for j in range(image_width):
            pixel_color = Vec3(float(i) / (image_width - 1), float(j) / (image_height - 1), 0.0)
            write_color(sys.stdout, pixel_color)

    sys.stderr.write("\rDone.                 \n")
    

if __name__ == "__main__":
    main()

