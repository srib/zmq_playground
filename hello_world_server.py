#!/usr/bin/python

import time
import zmq

def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:

        message = socket.recv()
        print("Received request: %s" % message )

        time.sleep(1)

        socket.send("World")

if __name__=="__main__":
    run_server()

