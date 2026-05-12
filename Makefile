M ?= 01
E ?= 1
F ?= *.py

run:
	python3 module$(M)/ex$(E)/$(F)

f:
	flake8 .

m:
	mypy .

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

.PHONY: clean flake mypy run