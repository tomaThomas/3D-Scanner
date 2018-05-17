#!/usr/bin/python
import stepper
import time
import cam

def run():
    while True:
        img = cam.capture_image()
        cam.save_image(img, '../test.png')
        stepper.step()
        time.sleep(1)

if __name__ == "__main__":
    run()
