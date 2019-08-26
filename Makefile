install:
	@pip install poetry
	@poetry install

isort:
	@isort -rc nomade tests

flake8:
	@flake8 nomade tests

black:
	@black nomade tests -S -l 79

codecheck: flake8
	@black nomade tests --check -S -l 79

runtests:
	@pytest -vv --cov-report term-missing --cov=nomade tests/

documentation:
	@sphinx-apidoc -f -o docs nomade
	@(cd docs; make html)
