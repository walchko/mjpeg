pistreamer
=========================

.. .. image:: https://travis-ci.org/walchko/hostinfo.svg?branch=master
.. 	:alt: Travis-ci
..     :target: https://travis-ci.org/walchko/hostinfo
.. .. image:: https://img.shields.io/pypi/v/hostinfo.svg
.. 	:alt: Latest Version
..     :target: https://pypi.python.org/pypi/hostinfo/
.. .. image:: https://img.shields.io/pypi/l/hostinfo.svg
.. 	:alt: License
..     :target: https://pypi.python.org/pypi/hostinfo/
.. .. image:: https://api.codacy.com/project/badge/Grade/0e28e971366e4abfaf79c668d19d8356
..    :alt: Codacy Badge
..    :target: https://www.codacy.com/app/kevin-walchko/hostinfo?utm_source=github.com&utm_medium=referral&utm_content=walchko/hostinfo&utm_campaign=badger
..

This is just a template that works for me.

Install
--------

.. The preferred way is to use ``pip`` with `pypi.org <https://pypi.python.org/pypi>`_ ::
..
.. 	pip install hostinfo
..
.. For development you can also do::
..
.. 	git clone https://github.com/walchko/package.git
.. 	cd package
.. 	pip install -r requirements.txt
.. 	pip install -e .
..
.. To test/build and publish::
..
.. 	python setup.py make
.. 	python setup.py publish
..
.. This will do both python 2.7 and python 3.x as both source and wheel packages.

Usage
------

http://stackoverflow.com/questions/1660045/what-is-the-difference-between-basehttpserver-and-simplehttpserver-when-and-whe

BaseHTTPServer is a HTTP server library. It understands the HTTP protocol and let's your code to handle requests. It doesn't have any "logic" on it's own. SimpleHTTPServer is built on top of BaseHTTPServer and handles requests in a similar way normal HTTP servers do, i.e. serve files from the file-system. In most cases you will want only BaseHTTPServer, as a base for implementing some development server for a web application.

If you are interested in working on a web application, not writing a HTTP server, you are probably looking for the WSGI interface. It allows you to write web aplications without depending on a specific server. There are also multiple frameworks that simplify the process.

Changes
--------

.. =============  ========  ======
.. Date           Version   Notes
.. =============  ========  ======
.. 2017-01-21     0.1.0     init
.. =============  ========  ======

MIT License
---------------

Copyright (c) 2017 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
