#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import package
import pkg_resources
import argparse
# from hostinfo.qr_code import QRCode


def handleArgs():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description="""
package
""")
	parser.add_argument('-e', '--ethernet', help='ethernet interface, default is eth0', default='eth0')
	parser.add_argument('-p', '--port', help='port, default is 9000', type=int, default=5000)
	parser.add_argument('-i', '--ip', help='host ip address, default is 0.0.0.0', default='0.0.0.0')
	parser.add_argument('--version', action='version', version=package.__version__)

	return vars(parser.parse_args())


def main():
	print('hello')
	print(pkg_resources.resource_filename('package', 'templates'))


if __name__ == '__main__':

	args = handleArgs()
	print('args', args)

	main()
