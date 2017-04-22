#!/usr/bin/python

from __future__ import print_function
import cv2
import SimpleHTTPServer
import SocketServer
import os

PORT = 8000


class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		possible_name = self.path.strip("/")+'.html'
		if self.path == '/':
			# default routing, instead of "index.html"
			self.path = '/simplehttpwebpage_content.html'
		elif os.path.isfile(possible_name):
			# extensionless page serving
			self.path = possible_name

		return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyRequestHandler

httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
