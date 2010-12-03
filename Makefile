PYTHON=python

all: build_ext build install

build_ext:
	${PYTHON} setup.py build_ext

build:
	${PYTHON} setup.py build

install:
	${PYTHON} setup.py install
