from PIL import Image


im = Image.open('img.jpeg')

box = (100,100,400,400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

im.save('rotate.jpeg')