run:
	docker-compose up -d

stop:
	docker-compose down

build: purge
	docker-compose build

purge:
	docker-compose down --remove-orphans

logs:
	docker-compose logs -tf

pre-deps:
	pip install pipenv

install: pre-deps
	pipenv sync --dev

update-deps: pre-deps
	pipenv update --dev

lint:
	pipenv run flake8 .
	pipenv run isort --check .
	pipenv run black --check .
	pipenv run mypy .

format:
	pipenv run isort .
	pipenv run black .

test:
	pipenv run pytest

test-coverage:
	pipenv run pytest --cov-report term --cov-report html --cov=ipos ipos/tests/

update-pre-commit:
	pre-commit autoupdate
