from imtools import get_imlist
import os

imges = get_imlist(os.getcwd())

for i in imges:
    print(i)
