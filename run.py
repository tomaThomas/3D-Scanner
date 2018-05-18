#!/usr/bin/python
import stepper
import time
import cam
import os


def run():
    file = open("/home/pi/3D-Scanner/LOCK","w")
    file.write(str(os.getpid()))
    file.close()
    x=3
    while x>0:
        x-=1
        img = cam.capture_image()
        cam.save_image('web-interface/test.png', img)
        stepper.step()
        time.sleep(1)
    os.remove("/home/pi/3D-Scanner/LOCK")


if __name__ == "__main__":
    run()
