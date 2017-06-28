import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
# MESSAGE = {"Acceleration":{"x": 10}, "Velocity":{"x": 10, "y": 20}, "Brake Status":{"x": 10, "y": 20}, "Lane Offset":{"x": 10, "y": 20}}
MESSAGE = '1|2|3|4|7|6|7|8|9|10|11'
# json_data = json.dumps(MESSAGE)
sock.sendto(MESSAGE, ("10.0.0.189", 8001))
# sock.sendto(bytes(MESSAGE, "utf-8"), ("10.0.0.189", 8001))