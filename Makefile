help:  ## Show this helper
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

install:  ## Install poetry and project dependencies
	@pip install poetry
	@poetry install

isort:  ## Apply isort to sort imports
	@isort -rc nomade tests

flake8:  ## Apply flake8 code check
	@flake8 nomade tests

black:  ## Apply black code formatter
	@black nomade tests

codecheck: flake8  ## Run code check with flake8 and black)
	@black nomade tests --check

runtests:  ## Run tests with pytest and generate code coverage with pytest-cov
	@pytest -vv --cov-report term-missing --cov=nomade tests/

security:  ## Run security checks using bandit
	@bandit -rv nomade

documentation:  ## Make the HTML documentation with sphinx
	@sphinx-apidoc -f -o docs nomade
	@(cd docs; make html)
