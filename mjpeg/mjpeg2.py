#!/usr/bin/env python3

import cv2
from flask import Flask, render_template, Response
import argparse


class VideoCamera(object):
	def __init__(self):
		# Using OpenCV to capture from device 0. If you have trouble capturing
		# from a webcam, comment the line below out and use a video file
		# instead.
		self.video = cv2.VideoCapture(0)
		# If you decide to use video.mp4, you must have this file in the folder
		# as the main.py.
		# self.video = cv2.VideoCapture('video.mp4')

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


def gen(camera):
	# i think this works better in py3 than py2
	while True:
		frame = camera.get_frame()
		yield (
			b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
		)


@app.route('/video_feed')
def video_feed():
	return Response(gen(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')


def handleArgs():
	parser = argparse.ArgumentParser(description='A simple mjpeg server Example: mjpeg-server -p 8080 --camera 4')
	parser.add_argument('-p', '--port', help='mjpeg publisher port, default is 9000', type=int, default=9000)
	# parser.add_argument('-c', '--camera', help='set opencv camera number, ex. -c 1', type=int, default=0)
	# parser.add_argument('-t', '--type', help='set camera type, either pi or cv, ex. -t pi', default='cv')
	parser.add_argument('-i', '--ip', help='set host', default='0.0.0.0')
	parser.add_argument('-s', '--size', help='set size', nargs=2, type=int, default=(320, 240))

	args = vars(parser.parse_args())
	args['size'] = (args['size'][0], args['size'][1])
	return args


if __name__ == '__main__':
	args = handleArgs()
	app.run(host=args['ip'], port=args['port'], debug=False)
