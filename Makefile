all: install test

install:
	python setup.py install

test:
	specloud tests
