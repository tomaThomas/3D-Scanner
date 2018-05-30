#import picamera
import PIL
from PIL import Image
import time
import numpy as np

width = 320  # Multiple of 32
height = 240  # Multiple of 16

# init camera
#camera = picamera.PiCamera()
#camera.resolution = (width, height)
time.sleep(2)

#image = np.empty((height, width, 3), dtype=np.uint8)  # Creates empty 3-dimensional numpy array (rows, columns, color)


def get_image():
    global image
    global camera
    camera.capture(image, 'rgb')  # Fills array with current picture


img = PIL.Image.open('testimg.jpg')

hsvimg = img.convert("HSV")
hsvimg.show()

array = np.array(img)
hsvarray = np.array(hsvimg)

i = array.shape[0]
j = array.shape[1]
for k in range(0, 10):
    for l in range(0, 10):
        print(array[k][l], hsvarray[k][l])