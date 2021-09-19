'''
此程序击破的伞兵：“我写了一堆乱码”
'''

from PIL import Image, ImageDraw,ImageSequence

def img2char(imgobj):
    scale = 5
    width, height = (int(imgobj.width/scale),int(imgobj.height/scale))
    img_original = imgobj.resize((width,height))
    img = imgobj.convert("L").resize((width,height))
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''

    img_new = Image.new("RGB", (width*scale, height*scale), "white")
    draw = ImageDraw.Draw(img_new)

    txt=""
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray/256*70)
            txt = ASCII_HIGH[index] + ' '
            color = img_original.getpixel(pos)
            draw.text((x*12, y*15), txt, fill=color)

    return img_new

def gif2char(imgfile):
    img = Image.open(imgfile)
    frames = ImageSequence.Iterator(img)
    img_colorchars = []
    for frame in frames:
        colorchar = img2char(frame)
        img_colorchars.append(colorchar)
    img_colorchars[0].save("bcm_colorchar.gif",append_images=img_colorchars[1:],loop=0,save_all=True)

gif2char("bcm.gif")
