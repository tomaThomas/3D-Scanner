from .gpio import *
import asyncio
import math

startPin = 2
time_per_step = 0.002
steps_per_scan = 100
step_angle = 2 * math.pi / steps_per_scan
current_angle = 0

print("Init stepper")


def get_steps_per_scan():
    return steps_per_scan


def get_current_angle():
    return current_angle


async def scan_step():
    global current_angle
    steps = 800*4/steps_per_scan
    for i in range(0, int(steps)):
        await stepper_step()
    current_angle += step_angle


async def stepper_step():
    gpio.set(1, True)
    await asyncio.sleep(time_per_step)
    gpio.set(1, False)
    await asyncio.sleep(time_per_step)


def cleanup():
    gpio.cleanup()


gpio.init(startPin)
