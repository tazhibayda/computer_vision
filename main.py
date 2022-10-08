from PIL import Image
from numpy import *

im = array(Image.open('img.jpeg').convert('L'))
im2 = 255 - im

im3 = (100.0/255) * im + 100
im4 = 255.0 * (im/255.0) ** 2

print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

pil_im = Image.fromarray(uint8(im2))
pil_im.show()