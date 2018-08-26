import PIL
from PIL import Image, ImageDraw
import random
import time
import math

inputImage = "reinhardt.png"
auxImage1 = "triggered.jpg"

duration = 40
#Generate frames in a list
names = ['img{:02d}.png'.format(i) for i in range(4)]

#Open Images
img = Image.open(inputImage)
triggImg = Image.open("triggered.jpg")

#Convert image to jpg
rgbimg = img.convert('RGB')
img = rgbimg

#Adding a red effect to an image
redimg = Image.open("red.jpg")
p, q = img.size
redimg = redimg.resize((p, q), Image.ANTIALIAS)
h, k = redimg.size
print(p, q, h, k, img.mode, redimg.mode)
blendedimg = Image.blend(img, redimg, 0.4)
img = blendedimg

#Adding the "triggered" to an image
newimg = img
p, q = newimg.size
newimg = newimg.crop((0,0,p,q+math.ceil(q/6)))
p, q = newimg.size
newTrigg = triggImg.resize((p, math.ceil(q/6)), Image.ANTIALIAS)
newimg.paste(newTrigg, (0, math.ceil(q-(q/6))))
newimg.save('test.png')
img = newimg

#Counter for the loop
i = 1

#Generate shaking gif individual images
for n in names:
    frame = img.copy()
    if i % 4 == 1 :
        c = 5
        f = 0
    elif i % 4 == 2 :
        c = -5
        f = 0
    elif i % 4 == 3 :
        c = 0
        f = 5
    else :
        c = 0
        f = -5

    a = 1
    b = 0
    d = 0
    e = 1
    img = img.transform(img.size, Image.AFFINE, (a, b, c, d, e, f))

    #img.save('image.png')
    frame.save(n)
    i = i+1

#Add generated images to a list
images = []
for n in names:
    frame = Image.open(n)
    #Crop images before appending
    w, h = frame.size
    cropped_img = frame.crop((5, 5, w-5, h-5))
    images.append(cropped_img)

#Generate the gif
images[0].save('circle.gif', save_all = True, append_images = images[1:], duration = duration, loop = 0)
