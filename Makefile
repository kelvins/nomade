init:
	@pip install poetry
	@poetry install

flake8:
	@flake8 nomade tests

test:
	@pytest -vv --cov-report term-missing --cov=nomade tests/
