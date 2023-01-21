install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish: install lint build
	poetry config repositories.test-pypi https://test.pypi.org/legacy/
	poetry publish -r test-pypi

lint:
	poetry run flake8 gendiff

package-install: install lint build
	python3 -m pip install --force-reinstall dist/*.whl