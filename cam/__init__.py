
import cv2

cap = cv2.VideoCapture(0)


def capture_image():
    rat, frame = cap.read()
    return frame


def save_image(img, path):
    cv2.imwrite(img, path)
