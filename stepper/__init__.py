from .gpio import *
import asyncio
import math

startPin = 2
pause = 0.002
steps_per_scan = 100
angle = 2*math.pi/steps_per_scan

print("Init stepper")


def get_angle():
    return angle


async def next_step():
    steps = 800/steps_per_scan
    for i in range(0, steps):
        await step()


async def rotate(degrees):
    print("rotating " + str(degrees) + " degrees")
    steps = int(degrees * 4.0 * 4.0 * 200.0 / 360.0)
    for i in range(0, steps):
        await step()


async def step():
    gpio.set(1, True)
    await asyncio.sleep(pause)
    gpio.set(1, False)
    await asyncio.sleep(pause)


def cleanup():
    gpio.cleanup()


gpio.init(startPin)
