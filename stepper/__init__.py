import gpio
import time

startPin = 22

print("Init stepper")

def rotate(degrees):
    print("rotating " + str(degrees) + " degrees")

def step():
    pause = 0.1
    print("moving step")
    gpio.setGPIOs(1,0,0,1)
    time.sleep(pause)
    gpio.setGPIOs(1,0,0,0)
    time.sleep(pause)
    gpio.setGPIOs(1,1,0,0)
    time.sleep(pause)
    gpio.setGPIOs(0,1,0,0)
    time.sleep(pause)
    gpio.setGPIOs(0,1,1,0)
    time.sleep(pause)
    gpio.setGPIOs(0,0,1,0)
    time.sleep(pause)
    gpio.setGPIOs(0,0,1,1)
    time.sleep(pause)
    gpio.setGPIOs(0,0,0,1)

gpio.init(startPin)
