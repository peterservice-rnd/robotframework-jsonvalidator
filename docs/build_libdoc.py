# -*- coding: utf-8 -*-
"""Script to generate library documentation using module libdoc."""

from os.path import dirname, join, realpath
from robot.libdoc import libdoc


DOCS_DIR = dirname(__file__)
SRC_DIR = realpath(join(DOCS_DIR, '..', 'src'))
LIB_NAME = 'JsonValidator'

if __name__ == '__main__':
    libdoc(join(SRC_DIR, LIB_NAME + '.py'), join(DOCS_DIR, LIB_NAME + '.html'), version='1.0.0')
