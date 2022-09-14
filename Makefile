.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python3 -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr test_results/
	rm -f *report.html
	rm -f log.html
	rm -f test-results.html
	rm -f output.xml

bootstrap:
	- python -m pip uninstall distro-info
	- poetry lock
	poetry install

build: clean ## builds source and wheel package
	poetry build

lint: ## check style with flake8
	poetry run flake8 --max-line-length=120 --ignore E501 src tests

test: clean ## run tests quickly with the default Python
	poetry run pytest

test-debug: ## run tests quickly with the default Python
	poetry run pytest --pdb

test-coverage: clean ## check code coverage quickly with the default Python
	mkdir -p ./test_results \
	&& PYTHONPATH=src poetry run pytest --cov=src tests/ --cov-report html --html=./test_results/index.html --self-contained-html
	mv htmlcov ./test_results/

test-acceptance: clean
	mkdir -p ./test_results/robot \
	&& cd ./test_results/robot \
	&& PYTHONPATH=../../src poetry run robot ../../tests/robot/

prepare-results:
	cp ./test_results/robot/report.html ./test_results/index.html

test-all: test-coverage test-acceptance

cibuild: test-coverage test-acceptance build

run:
	poetry run python3 -m levelup
