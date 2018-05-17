
import cv2

cap = cv2.VideoCapture(0)


def capture_image():
    print("Capturing image")
    ret, frame = cap.read()
    return frame


def save_image(path, img):
    print("Saving image " + path)
    cv2.imwrite(path, img)
