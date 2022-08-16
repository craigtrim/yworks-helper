install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build

all:
	make build
	poetry run python -m pip install --upgrade pip

jupyter:
	poetry run python -m ipykernel install --name bastbox
	poetry run jupyter notebook
