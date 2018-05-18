#!/usr/bin/python
# import stepper
import time
import cam
import os


def run():
    file = open("LOCK", "w")
    file.write(str(os.getpid()))
    file.close()
    x = 0
    while x < 3:
        img = cam.capture_image()
        cam.save_image('web-interface/test.png', img)
        # stepper.step()
        time.sleep(1)
        x += 1

    os.remove("LOCK")


if __name__ == "__main__":
    run()
