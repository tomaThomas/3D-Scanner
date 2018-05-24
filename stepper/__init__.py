from .gpio import *
import asyncio

startPin = 2
pause = 0.002
angle = "whatever"  # TODO

print("Init stepper")


def get_angle():
    return angle


def next_step():
    rotate(angle)


async def rotate(degrees):
    print("rotating " + str(degrees) + " degrees")
    steps = int(degrees * 4.0 * 4.0 * 200.0 / 360.0)
    for i in range(0, steps):
        await step()


async def step():
    print("moving step")
    gpio.set(1, True)
    await asyncio.sleep(pause)
    gpio.set(1, False)
    await asyncio.sleep(pause)


def cleanup():
    gpio.cleanup()


gpio.init(startPin)
