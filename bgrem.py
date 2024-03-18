import rembg
from PIL import Image
#img_open=Image.open('army.jpg')
img_open=rembg.remove(Image.open('4dogs.jpg'))
img_open.save('dogs.png')

