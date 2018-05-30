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

array = np.array(img)


hsvarray = np.array(hsvimg)
hsvarray = hsvarray.astype(float)

hsvarray = np.add(hsvarray[:, :], [-237, -70, -255], casting='unsafe')
hsvarray = np.multiply(hsvarray, hsvarray, casting='unsafe')
hsvarray = np.multiply(hsvarray[:, :], [0.010, 0.005, 0.0008], casting='unsafe')

hsvarray = hsvarray.sum(axis=2)
hsvarray = np.clip(hsvarray, 0, 255)
hsvarray = hsvarray.astype(np.uint8)



showimg = PIL.Image.fromarray(hsvarray)
showimg.show()


# i = array.shape[0]
# j = array.shape[1]
# for k in range(0, i):
#     print("k" + str(k))
#     for l in range(0, j):
#         print(l)
#         h = hsvarray[k][l][0]
#         s = hsvarray[k][l][1]
#         v = hsvarray[k][l][2]
#
#         hsvarray[k][l][0] = int(((1.4 * (h-237) ** 2) + (0.05 * (s-70) ** 2) + (0.008 * (v - 255) ** 2))*0.5)
#         if hsvarray[k][l][0] > 255:
#             hsvarray[k][l][0] = 255
#         hsvarray[k][l][1] = 0
#         hsvarray[k][l][2] = 0
#
# showimg = PIL.Image.fromarray(hsvarray)
# showimg.show()