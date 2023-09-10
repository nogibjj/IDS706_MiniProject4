# Makefile
setup:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8

.PHONY: setup test lint
