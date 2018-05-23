import cv2
import base64

cap = cv2.VideoCapture(0)

def set_width(value):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, value)
def set_height(value):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, value)
def set_brightness(value):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, value)
def set_contrast(value):
    cap.set(cv2.CAP_PROP_CONTRAST, value)
def set_saturation(value):
    cap.set(cv2.CAP_PROP_SATURATION, value)
def set_hue(value):
    cap.set(cv2.CAP_PROP_HUE, value)
def set_gain(value):
    cap.set(cv2.CAP_PROP_GAIN, value)
def set_exposure(value):
    cap.set(cv2.CAP_PROP_EXPOSURE, value)


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
