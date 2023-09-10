# Makefile
setup:
	pip install -r requirements.txt

test:
	/usr/bin/python3.8 -m pytest

lint:
	/usr/bin/python3.8 -m flake8

.PHONY: setup test lint
