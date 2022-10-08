from pylab import *
from PIL import Image


im = array(Image.open('img.jpeg').convert('L'))

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)
show()
