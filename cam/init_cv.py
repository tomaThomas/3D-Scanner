import cv2
import base64
import numpy

cap = cv2.VideoCapture(0)


def get_list():
    return numpy.array()


def set_width(value):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, float(value))


def set_height(value):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, float(value))


def set_brightness(value):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, float(value))


def set_contrast(value):
    cap.set(cv2.CAP_PROP_CONTRAST, float(value))


def set_saturation(value):
    cap.set(cv2.CAP_PROP_SATURATION, float(value))


def capture_image():
    print('Capturing image')
    ret, frame = cap.read()
    return frame


def save_image(path, img):
    print('Saving image ' + path)
    cv2.imwrite(path, img)


def image_encode(img):
    if img is not None:
        ret, buf = cv2.imencode('.png', img)
        res = (base64.b64encode(buf).decode('ascii'))
        return res
    return ''
