#!/usr/bin/python
# import stepper
import cam
import os
import asyncio
import websockets

running = False


async def msg_receive(socket, path):
    print("client connected")
    global running
    async for msg in socket:
        print("message received: {}".format(msg))
        if msg == "pid":
            await socket.send("pid={}".format(os.getpid()))
        elif msg == "running":
            await socket.send("running={}".format(running))
        elif msg == "start":
            running = True
        elif msg == "stop":
            running = False
        elif msg == "quit":
            request_exit()
        else:
            print("unknown command: {}".format(msg))


async def main_loop():
    print("main loop started")
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
    # acquire lock
    file = open("LOCK", "w")
    file.write(str(os.getpid()))
    file.close()

    print("starting event loop")
    loop = asyncio.get_event_loop()

    open_socket = websockets.serve(msg_receive, 'localhost', 8765)
    loop.run_until_complete(open_socket)

    asyncio.async(main_loop())

    # TODO: implement graceful exit
    # for sig in (signal.SIGINT, signal.SIGTERM):
    #     loop.add_signal_handler(sig, request_exit)

    loop.run_forever()
    loop.close()
    print("closed event loop")

    # release lock
    os.remove("LOCK")


if __name__ == "__main__":
    main()
