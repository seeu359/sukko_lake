run:
	poetry run python manage.py runserver

makemigrate:
	poetry run ./manage.py makemigrations sukko_lake

migrate:
	poetry run python manage.py migrate

lint:
	poetry run flake8

p_install:
	poetry install

install:
	pip install -r requirements.txt

sort:
	poetry run isort .