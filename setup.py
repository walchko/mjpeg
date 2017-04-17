from setuptools import setup
from hostinfo.version import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution


PACKAGE_NAME = 'pimjpeg'
BuildCommand.pkg = PACKAGE_NAME
# BuildCommand.py2 = False
# BuildCommand.py3 = False
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
README = open('README.rst').read()
GITHUB = "https://github.com/walchko/{}".format(PACKAGE_NAME)
INSTALL_REQ = open("requirements.txt").readlines()
TEST_REQ = ['nose']
CMDS = {'publish': PublishCommand, 'make': BuildCommand}


setup(
	name=PACKAGE_NAME,
	version=VERSION,
	author="Kevin J. Walchko",
	keywords=['package', 'keywords'],
	author_email="kevin.walchko@outlook.com",
	description="raspbery pi camera mjpeg streamer",
	license="MIT",
	package_data={
		'package': ['templates', 'static'],
	},
	include_package_data=True,
	zip_safe=False,
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Operating System :: Unix',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Topic :: Utilities',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: System :: Shells',
		'Environment :: Console'
	],
	install_requires=INSTALL_REQ,
	tests_require=TEST_REQ,
	url=GITHUB,
	long_description=README,
	cmdclass=CMDS,
	packages=[PACKAGE_NAME],
	# scripts=[
	# 	'bin/hello.py'
	# ]
)
