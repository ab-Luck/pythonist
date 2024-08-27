import rembg
from PIL import Image
#img_open=Image.open('army.jpg')
img_open=rembg.remove(Image.open('blackwomenhbag.jpg'))
img_open.save('blackwomenhbag.png')

