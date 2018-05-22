from .gpio import *
import asyncio

startPin = 2

print("Init stepper")


async def rotate(degrees):
    print("rotating " + str(degrees) + " degrees")
    steps = int(degrees * 4.0 * 200.0 / 360.0)
    for i in range(0, steps):
        await step()


async def step():
    pause = 0.1
    print("moving step")
    gpio.set(1, True)
    asyncio.sleep(pause)
    gpio.set(1, False)
    asyncio.sleep(pause)


def cleanup():
    gpio.cleanup()


gpio.init(startPin)
