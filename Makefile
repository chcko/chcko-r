.PHONY: check html dist up

check:
	restview --long-description --strict

html:
	cd chcko/r
	doit -kd. html
	doit -kd. initdb

dist:
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`



