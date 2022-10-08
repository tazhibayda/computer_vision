from PIL import Image

im = Image.open('img.jpeg').convert('L').save('image_L_MODE.jpeg')

print(im)