import PIL
from PIL import Image, ImageDraw

names = ['img{:02d}.png'.format(i) for i in range(20)]
im = Image.new("RGB", (200,200), 'green')

pos = 0
for n in names:
    frame = im.copy()
    draw = ImageDraw.Draw(frame)
    draw.ellipse((pos, pos, 50+pos, 50+pos), 'red')
    frame.save(n)
    pos += 10

images = []

for n in names:
    frame = Image.open(n)
    images.append(frame)

images[0].save('circle.gif', save_all = True, append_images = images[1:], duration = 100, loop = 0)
