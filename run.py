#!/usr/bin/python
import stepper
import time

def run():
    while True:
        stepper.step()
        time.sleep(1)

if __name__ == "__main__":
    run()
