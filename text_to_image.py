from PIL import ImageFont, Image, ImageDraw

open_sans_light = ImageFont.truetype("fonts/Open_Sans/OpenSans-Light.ttf", 100)

imageFile = "images/elijah1.jpg"
image = Image.open(imageFile).convert('RGBA')

draw = ImageDraw.Draw(image)
draw.text((10,10), 'ASA', font=open_sans_light, fill=(255,255,255))
draw = ImageDraw.Draw(image)
# image.show()

img2 = Image.new('RGBA', (1000, 1000), color = (164, 75, 24))
d = ImageDraw.Draw(img2)
d.text((10,10), "ASA", fill=(255,255,0), font=open_sans_light)
d = ImageDraw.Draw(img2)
img2.show()

"""
to do:

multiline text: https://stackoverflow.com/questions/7698231/python-pil-draw-multiline-text-on-image
center text: https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
create classes to store information
command line text entry
create images with different colors
"""
