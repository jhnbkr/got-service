.PHONY: install run release web

install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

release:
	python manage.py migrate

web:
	gunicorn project.wsgi --log-file -
