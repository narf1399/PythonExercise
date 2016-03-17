#!/usr/bin/env python

from distutils.core import setup

setup(
	name='hello_world_module',
	version='1.0',
	description='Module to print some message',
	author='Tim Metzler',
	packages=['hello_world_module'],
	package_dir={'':'src'}
)
