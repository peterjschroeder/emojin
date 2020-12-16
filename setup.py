#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='emojin', 
        version='0.1', 
        description='TUI emoji selector that outputs to WeeChat.', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/emojin',
        scripts=['emojin'],
        install_requires=['urwid']
)

