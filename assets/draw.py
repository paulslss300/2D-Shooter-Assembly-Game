from PIL import Image
import numpy as np

if __name__ == "__main__":
    lst = []
    with Image.open("bg.png") as im:
        rgb_im = im.convert('RGB')
        for y in range(rgb_im.size[1]):
            for x in range(rgb_im.size[0]):
                color = rgb_im.getpixel((x, y))
                if color == (255, 255, 255):
                    hex_value = '0x%02x%02x%02x' % (0, 0, 0)
                else:
                    hex_value = '0x%02x%02x%02x' % (color[0], color[1], color[2])
                lst.append(hex_value)

    print(len(lst))

    with open("outfile", "w") as outfile:
        outfile.write(", ".join(lst))
