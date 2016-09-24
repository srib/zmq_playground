#!/usr/bin/python

import zmq

def run_client():
  context = zmq.Context()
  
  print("Connecting to hello world server..")
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5555")
  
  for request in range(10):
    print("Sending request %s..." % request)
    socket.send("Hello")
    
    # Get reply and print
    
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

if __name__ == "__main__":
      run_client()
