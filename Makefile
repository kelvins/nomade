install:
	@pip install poetry
	@poetry install

isort:
	@isort -rc nomade tests

flake8:
	@flake8 nomade tests

black:
	@black nomade tests --check -S -l 80

runtests:
	@pytest -vv --cov-report term-missing --cov=nomade tests/
