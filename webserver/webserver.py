#!/usr/bin/env python

from flask import Flask
# from flask import flash
from flask import render_template
from flask import url_for
# from flask import Response

data = {
	'power': 75,  # gauge
	'leg1': [1, 2, 3],  # leg angles
	'leg2': [1, 2, 3],  # leg angles
	'leg3': [1, 2, 3],  # leg angles
	'leg4': [1, 2, 3],  # leg angles
	'status': 'running',  # running | stop | error_stop
	'compass': 31.234,  # heading
	'ir': [12, 10, 0, 20],  # ir ranges
	'msgs': [  # max 20 messages
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
		'2017/2/11 13:23 [error] this is a message: 3.67 5.666 -1234.567',
	]
}


i = [12, 19, 3, 17, 28, 24, 7]

app = Flask(__name__)
# app.secret_key = 'random string'


@app.route('/')
def index():
	# print url_for('static', filename='info.js')
	return render_template('chart.html', num=i)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(host='localhost', port=9000, debug=False)
