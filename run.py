#!/usr/bin/python
import stepper
import linearalgebra
import exporter
import asyncio
import websockets
import json
import cam
import datetime

running = False

lastPoints = {'points': []}


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
                if not running:
                    asyncio.ensure_future(scan())
                    running = True
                await socket.send(json.dumps({"running": running}))
            if "stop" in msg_parsed:
                running = False
                await socket.send(json.dumps({"running": running}))
            if "stepper" in msg_parsed:
                for a in range(0, stepper.get_steps_per_scan()):
                    await stepper.scan_step()
            if "points" in msg_parsed:
                await socket.send(json.dumps(lastPoints))

    except websockets.exceptions.ConnectionClosed:
        print("client disconnected")


async def scan():
    global running
    global lastPoints
    running = True
    exporter.create()
    steps = stepper.get_steps_per_scan()
    for i in range(steps):
        if not running:
            break
        print("step " + str(i))
        points = await cam.get_points()

        points_transformed = await linearalgebra.transform(points, stepper.get_current_angle())

        exporter.add_row(points_transformed)

        print(exporter.point_list)

        point_json = {'points': []}
        for p in range(len(exporter.point_list)):
            point_json['points'].append({'point': exporter.point_list[p].tolist()})

        lastPoints = point_json

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
