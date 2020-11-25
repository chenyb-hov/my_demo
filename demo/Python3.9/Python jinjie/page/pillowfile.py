from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# image = Image.open('D:/Users/season/Desktop/favicon.ico')
# w, h = image.size
# print('width: %s, height: %s' % (w, h))
#
# image.thumbnail((w * 2, h * 2))
# print('rw: %s, rh: %s' % (2 * w, 2 * h))
# image.save('favicon.png', 'png')

def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

withs = 60 * 4
heights = 60
image1 = Image.new('RGB', (withs, heights), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)

draw = ImageDraw.Draw(image1)

yzm = []
for i in range(4):
    rnd = rndChar()
    yzm.append(rnd)
    draw.text((60 * i + 10, 10), rnd, font = font, fill = rndColor2())

image2 = image1.filter(ImageFilter.BLUR)
image2.save('code.jpg', 'jpeg')
print(yzm)