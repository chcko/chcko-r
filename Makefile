.PHONY: check dist up

check:
	restview --long-description --strict

dist:
	cd chcko/r
	doit -kd. html
	doit -kd. initdb
	cd ../..
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`



