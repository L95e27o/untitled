import os
import glob
from PIL import Image


def thumbnail_pic(path):

    a = glob.glob(path+'\\*.jpg')
    for i in a:

        name = os.path.join(path, i)
        im = Image.open(name)
        im.thumbnail((1136, 640))
        print (im.format, im.size, im.mode)
        im.save(name, 'JPEG')
        im.close()
    print ('Done!')


if __name__ == "__main__":
    path = 'C:\Users\LH\PycharmProjects\untitled'
    thumbnail_pic(path)
