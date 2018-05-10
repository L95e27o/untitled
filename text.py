from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
im = Image.open(u'C:/test.jpg')

x = ImageDraw.Draw(im)

n = im.size

font = ImageFont.truetype('arial.ttf', 100)

x.text((n[0]*4/5,0),"7",fill = (500,0,0),font = font)

im.show()
im.save('output.jpg','JPEG')
