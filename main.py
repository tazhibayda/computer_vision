from PIL import Image

im = Image.open('img.jpeg').convert('L').save('image.jpeg')

print(im)