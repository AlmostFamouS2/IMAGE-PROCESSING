from PIL import Image, ImageFilter
import numpy as np
import os

DATA_DIR = os.path.join('IMAGE_PROCESSING')

def show_vertical(img, img2):
    im = Image.fromarray(np.vstack((np.array(img), np.array(img2))))
    im.show()

def show_horizontal(img, img2):
    im = Image.fromarray(np.hstack((np.array(img), np.array(img2))))
    im.show()


def funcs(ha = 1):
    ops = [img.filter(ImageFilter.BLUR), img.filter(ImageFilter.CONTOUR), img.filter(ImageFilter.EMBOSS)]
    return ops[ha]

img = Image.open(os.path.join(DATA_DIR, 'MEGA.jpg'))
filtered = funcs(2)

show_vertical(img, filtered)
show_horizontal(img, filtered)
