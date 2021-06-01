web:
	python web.py

migrations:
	alembic upgrade head

requirements:
	pip install -r requirements-dev.txt

start: requirements migrations web

test:
	pytest --cov=backend --cov-fail-under 100 --blockage  --cov-report term-missing

smoke-tests:
	pytest tests/smoke_tests

coverage-collect:
	coverage run -m pytest

coverage-report:
	coverage html

coverage: coverage-collect coverage-report

mypy:
	mypy backend tests *.py

flake8:
	flake8 .

isort:
	isort .

bandit:
	bandit -q -r -x /venv,/tests .

safety:
	safety check --bare --full-report -r requirements.txt -r requirements-dev.txt

check-licenses:
	check_licenses > /dev/null

check: smoke-tests isort flake8 mypy bandit safety check-licenses test

git-hooks:
	pre-commit install && pre-commit install -t pre-push
