#!/usr/bin/python
import stepper
import cam
import os
import asyncio
import websockets
import json

running = False

img = None


async def msg_receive(socket, path):
    print("client connected")
    global running
    global img
    try:
        await socket.send(json.dumps({"running": running}))
        while True:
            msg = await socket.recv()
            print("message received: {}".format(msg))
            msg_parsed = json.loads(msg)
            if "pid" in msg_parsed:
                await socket.send(json.dumps({"pid": os.getpid()}))
            if "running" in msg_parsed:
                await socket.send(json.dumps({"running": running}))
            if "start" in msg_parsed:
                running = True
                await socket.send(json.dumps({"running": running}))
            if "img" in msg_parsed:
                await socket.send(json.dumps({"img": cam.image_encode(img)}))
            if "stepper" in msg_parsed:
                for a in range(0,stepper.steps_per_scan):
                    await stepper.scan_step()
            if "stop" in msg_parsed:
                running = False
                await socket.send(json.dumps({"running": running}))
            if "quit" in msg_parsed:
                request_exit()
            if "width" in msg_parsed:
                cam.set_width(msg_parsed["width"])
            if "height" in msg_parsed:
                cam.set_height(msg_parsed["height"])
            if "brightness" in msg_parsed:
                cam.set_brightness(msg_parsed["brightness"])
            if "contrast" in msg_parsed:
                cam.set_contrast(msg_parsed["contrast"])
            if "saturation" in msg_parsed:
                cam.set_saturation(msg_parsed["saturation"])

    except websockets.exceptions.ConnectionClosed:
        print("client disconnected")


async def main_loop():
    print("main loop started")
    global img
    while True:
        try:
            if running:
                img = cam.capture_image()
                # cam.save_image('web-interface/test.png', img)
                # stepper.step()
            await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            print("stopping main loop")
            raise


async def stop_event_loop():
    loop = asyncio.get_event_loop()
    loop.stop()
    print("stopped event stopped")


def request_exit():
    for task in asyncio.Task.all_tasks():
        task.cancel()
    asyncio.async(stop_event_loop())


def main():
    # # acquire lock
    # file = open("LOCK", "w")
    # file.write(str(os.getpid()))
    # file.close()

    print("starting event loop")
    loop = asyncio.get_event_loop()

    open_socket = websockets.serve(msg_receive, '0.0.0.0', 8888)
    loop.run_until_complete(open_socket)

    asyncio.async(main_loop())

    # TODO: implement graceful exit
    # for sig in (signal.SIGINT, signal.SIGTERM):
    #     loop.add_signal_handler(sig, request_exit)

    loop.run_forever()
    loop.close()
    print("closed event loop")

    # # release lock
    # os.remove("LOCK")


if __name__ == "__main__":
    main()
