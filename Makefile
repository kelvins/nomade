install:
	@pip install poetry
	@poetry install

isort:
	@isort -rc nomade tests

flake8:
	@flake8 nomade tests

black:
	@black nomade tests

codecheck: flake8
	@black nomade tests --check

runtests:
	@pytest -vv --cov-report term-missing --cov=nomade tests/

documentation:
	@sphinx-apidoc -f -o docs nomade
	@(cd docs; make html)
