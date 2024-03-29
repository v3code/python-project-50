install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish: install lint test build
	poetry config repositories.test-pypi https://test.pypi.org/legacy/
	poetry publish -r test-pypi

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

package-install: install build
	python3 -m pip install --force-reinstall dist/*.whl