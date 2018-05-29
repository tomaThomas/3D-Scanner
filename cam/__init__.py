import picamera
import time
import numpy as np

width = 320  # Multiple of 32
height = 240  # Multiple of 16

# init camera
camera = picamera.PiCamera()
camera.resolution = (width, height)
time.sleep(2)

image = np.empty((height, width, 3), dtype=np.uint8)  # Creates empty 3-dimensional numpy array (rows, columns, color)


def get_image():
    camera.capture(image, 'rgb')  # Fills array with current picture
