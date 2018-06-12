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


async def msg_receive(socket, _):
    global running
    global mode
    print("client connected")
    try:
        await socket.send(json.dumps({"status": "Connection established"}))
        while True:
            msg = await socket.recv()
            print("message received: {}".format(msg))
            msg_parsed = json.loads(msg)
            if "running" in msg_parsed:
                await socket.send(json.dumps({"status": "Connection established"}))

            if "fastmode" in msg_parsed:
                if not running:
                    mode = "fast";
            if "highQuality" in msg_parsed:
                if not running:
                    mode = "highQuality"
            if "start" in msg_parsed:
                if not running:
                    if mode == "highQuality":
                        stepper.set_steps_per_scan(200)
                        stepper.calculate_step_angle()
                    else:
                        stepper.set_steps_per_scan(100)
                        stepper.calculate_step_angle()
                    asyncio.ensure_future(scan(socket))
                await socket.send(json.dumps({"status": "Scan started"}))
            if "stop" in msg_parsed:
                running = False
                await socket.send(json.dumps({"status": "Scan stopped"}))
            if "stepper" in msg_parsed:
                for a in range(0, stepper.get_steps_per_scan()):
                    await stepper.scan_step()

    except websockets.exceptions.ConnectionClosed:
        print("client disconnected")


async def scan(socket):
    global running
    global lastPoints
    running = True
    exporter.create()
    steps = stepper.get_steps_per_scan();
    for i in range(steps):
        if not running:
            break
        print("step " + str(i))
        progress_json = {'progress': (i/steps)*100}
        await socket.send(json.dumps(progress_json))
        points = await cam.get_points()

        points_transformed =  linearalgebra.transform(points, stepper.get_current_angle())

        exporter.add_row(points_transformed)

        #point_json = {'points': []}
        #for p in range(len(points)):
        #    point_json['points'].append({'point': points[p].tolist()})

        point_json = {'points': []}
        for p in range(len(points_transformed)):
            point_json['points'].append({'point': points_transformed[p].tolist()})

        await socket.send(json.dumps(point_json))

        await stepper.scan_step()

    name = "scan_" + str(datetime.datetime.now()).replace(" ", "_")
    url = {"url" : name}
    await socket.send(json.dumps(url))
    exporter.export(name)


    export_finished = {"exportFinished" : "true"}
    await socket.send(json.dumps(export_finished))
    running = False


def main():
    print("starting event loop")

    linearalgebra.init(cam.width, cam.height)

    loop = asyncio.get_event_loop()

    open_socket = websockets.serve(msg_receive, '0.0.0.0', 8888)
    loop.run_until_complete(open_socket)
    loop.run_forever()
    loop.close()

    print("closed event loop")


if __name__ == "__main__":
    main()
