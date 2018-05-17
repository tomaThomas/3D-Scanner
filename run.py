#!/usr/bin/python
import stepper
import time
import cam


def run():
    i = 0
    while True:
        img = cam.capture_image()
        cam.save_image('/web-interface/test' + str(i) + '.png', img)
        stepper.step()
        time.sleep(1)
        i+=1


if __name__ == "__main__":
    run()
