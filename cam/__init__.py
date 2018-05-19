
import cv2
import base64

cap = cv2.VideoCapture(0)


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
        res = (base64.b64encode(buf).decode('utf-8'))
        return res
    return ""
