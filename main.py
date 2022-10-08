from pylab import *
from PIL import Image


im = array(Image.open('img.jpeg'))
imshow(im)

x = [600, 600, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2])

title('Plotting: "img.jpeg"')
show()