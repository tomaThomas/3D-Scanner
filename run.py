#!/usr/bin/python
import stepper
import time
import cam


def run():
    x=3
    while x>0:
        x-=1
        img = cam.capture_image()
        cam.save_image('web-interface/test.png', img)
        stepper.step()
        time.sleep(1)


if __name__ == "__main__":
    run()
