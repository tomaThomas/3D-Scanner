
import cv2

cap = cv2.VideoCapture(0)


def capture_image():
    ret, frame = cap.read()
    return frame


def save_image(path, img):
    cv2.imwrite(path, img)
