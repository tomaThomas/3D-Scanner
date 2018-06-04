#!/usr/bin/python
import stepper
import linearalgebra
import exporter
import asyncio
import websockets
import json
import numpy
import datetime

running = False


async def msg_receive(socket, _):
    print("client connected")
    global running
    try:
        await socket.send(json.dumps({"running": running}))
        while True:
            msg = await socket.recv()
            print("message received: {}".format(msg))
            msg_parsed = json.loads(msg)
            if "running" in msg_parsed:
                await socket.send(json.dumps({"running": running}))
            if "start" in msg_parsed:
                scan()
                await socket.send(json.dumps({"running": running}))
            if "stop" in msg_parsed:
                running = False
                await socket.send(json.dumps({"running": running}))
            if "stepper" in msg_parsed:
                for a in range(0, stepper.get_steps_per_scan()):
                    await stepper.scan_step()

    except websockets.exceptions.ConnectionClosed:
        print("client disconnected")


async def scan():
    global running
    running = True
    exporter.create()
    steps = stepper.steps_per_scan
    for i in range(steps):
        if not running:
            break
        points = numpy.zeros((0, 2))  # points = await cam.get_points()
        points = await linearalgebra.transform(points, stepper.get_current_angle())
        exporter.add_row(points)
        await stepper.scan_step()

    exporter.export("scan_" + str(datetime.datetime.now()))
    running = False


def main():
    print("starting event loop")

    loop = asyncio.get_event_loop()

    open_socket = websockets.serve(msg_receive, '0.0.0.0', 8888)
    loop.run_until_complete(open_socket)
    loop.run_forever()
    loop.close()

    print("closed event loop")


if __name__ == "__main__":
    main()
