#!/usr/bin/env python

from distutils.core import setup

setup(
	name='cachedurl',
	version='0.1',
	author='Martin Czygan',
	author_email='martin.czygan@gmail.com',
	url='http://myyn.org',
	py_modules=['cachedurl'],
	description="""
		SHA256-based compressed URL cache infrastructure 
		as simple as it can get.""",
	long_description="""
		Save bandwidth and server resources through caching. 
		Default location is .cachedurlcache/ under user's home.""",
	license='BSD',
	platforms = ["any"],
	classifiers=["Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python", 
	],
)

