import picamera
import matplotlib

import numpy as np

width = 640  # Multiple of 32
height = 480  # Multiple of 16

# init camera
camera = picamera.PiCamera()
camera.resolution = (width, height)

async def get_points():
    global camera
    img = np.empty((height, width, 3), dtype=np.uint8)
    camera.capture(img, 'rgb', use_video_port=True)  # Fills array with current picture

    matplotlib.colors.rgb_to_hsv(img)

    # convert image to floating point for higher precision and range
    img = img.astype(float)

    # score each pixel in the image (operations are performed on every pixel)
    img += [-237, -70, -255]
    img *= img
    img *= [0.04, 0.00, 0.008]
    img = img.sum(axis=2)


# find indices of the best scoring pixel in each line
    best_pix = img.argmin(1)
    best_val = img[np.arange(img.shape[0]), best_pix]


    bestval_avg = np.average(best_val)
    avg = np.average(img)

    best_pix = np.stack((best_pix, np.arange(img.shape[0])), axis=1)

    best_pix = np.compress(best_val < (avg * 0.1 + bestval_avg * 1), best_pix, axis=0)


    return best_pix
