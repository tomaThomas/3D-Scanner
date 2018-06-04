# import picamera
import PIL
from PIL import Image
# import time
import numpy as np

width = 320  # Multiple of 32
height = 240  # Multiple of 16


# init camera
# camera = picamera.PiCamera()
# camera.resolution = (width, height)
# time.sleep(2)

# image = np.empty((height, width, 3), dtype=np.uint8)  # Creates empty 3-dimensional numpy array (rows, columns, color)


def get_image():
    global image
    global camera
    camera.capture(image, 'rgb')  # Fills array with current picture


orig_img = PIL.Image.open('old_testimg.jpg')
hsv_img = orig_img.convert("HSV")

img = np.array(hsv_img)
# convert image to floating point for higher precision and range
img = img.astype(float)

# score each pixel in the image (operations are performed on every pixel)
img += [-240, -70, -255]
img *= img
img *= [0.025, 0.005, 0.005]
img = img.sum(axis=2)

# find indices of the best scoring pixel in each line
best_pix = img.argmin(1)
best_val = img[np.arange(img.shape[0]), best_pix]

relative_best = best_val.min()
print("Bester Pixelwert:", relative_best)

best_pix = np.stack((np.arange(img.shape[0]), best_pix), axis=1)

best_pix = np.compress(best_val < (40 + 6 * relative_best), best_pix, axis=0)

# convert to displayable image
img = np.clip(img, 0, 255)
img = img.astype(np.uint8)

# make rgb from greyscale (to enable coloring)
img = img.reshape((img.shape[0], img.shape[1], 1))
img = np.repeat(img, 3, axis=2)

indices = np.split(best_pix, 2, axis=1)

img[indices[0], indices[1]] = [255, 0, 0]
# display image
PIL.Image.fromarray(img).show()
