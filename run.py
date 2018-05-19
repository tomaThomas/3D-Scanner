#!/usr/bin/python
# import stepper
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
            if msg == "pid":
                await socket.send(json.dumps({"pid": os.getpid()}))
            elif msg == "running":
                await socket.send(json.dumps({"running": running}))
            elif msg == "start":
                running = True
                await socket.send(json.dumps({"running": running}))
            elif msg == "img":
                await socket.send(json.dumps({"img": cam.image_encode(img)}))
            elif msg == "stop":
                running = False
                await socket.send(json.dumps({"running": running}))
            elif msg == "quit":
                request_exit()
            else:
                print("unknown command: {}".format(msg))
    except websockets.exceptions.ConnectionClosed:
        print("client disconnected")


async def main_loop():
    print("main loop started")
    global img
    while True:
        try:
            if running:
                img = cam.capture_image()
                cam.save_image('web-interface/test.png', img)
                # stepper.step()
            await asyncio.sleep(1)
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
