import os, socket, thread
from flask import Flask, render_template, jsonify, json
import parameters

global acceleration, velocity, brake, laneoff, x
acceleration = 0
velocity = 0
brake = 0
laneoff = 0
x = 0

def udp_receive():
	print 'start udp server ...'
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.bind((parameters.IP, parameters.UDP_PORT))

	while True:
		try:
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
			if '|' in data:
				print "vehicle data:"+data
				all_vehicle_data = data.split('|')
			try:
				global acceleration, velocity, brake, laneoff, x
				velocity = all_vehicle_data[4]
				brake = all_vehicle_data[8]
				acceleration = all_vehicle_data[9]
				laneoff = all_vehicle_data[10]

				x = x+1
			except Exception:
				pass
			
		except KeyboardInterrupt:
			break

try:
	thread.start_new_thread( udp_receive, ())
except:
	print "Error: unable to start thread"


app = Flask(__name__)

# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update')
def update():
	global x, y
	return jsonify({"Acceleration":{"x": x, "y": acceleration}, "Velocity":{"x": x, "y": velocity}, "BrakeStatus":{"x": x, "y": brake}, "LaneOffset":{"x": x, "y": laneoff}})

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host=parameters.IP, port=int(port))