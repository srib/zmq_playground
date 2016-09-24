#!/usr/bin/env python

import sys
import zmq

socket = zmq.Context().socket(zmq.SUB)

socket.connect("tcp://localhost:5556")

# print("Collecting updates from the weather server..")
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')

socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

total_temp = 0

for count in range(10):
    string = socket.recv_string()
    zipcode, temperature, humidity = string.split()
    total_temp += int(temperature)

print zip_filter, total_temp / (count+1)
