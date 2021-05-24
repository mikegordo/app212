.PHONY: default clean kill start test psql

default:
	@echo "\nBringing up the containers\n"
	docker-compose up -d --remove-orphans
	sleep 5
	@echo "\nRunning the DB creation script\n"
	docker exec -i $$(docker-compose ps -q db) psql -Upostgres < helpers/database_initialization.sql
	sleep 5
	@echo "\nApplying the migrations\n"
	make migrate
	@echo "\nPopulating the DB with data\n"
	DJANGO_SETTINGS_MODULE=data.settings.local python manage.py db_seed

migrate:
	DJANGO_SETTINGS_MODULE=data.settings.local python manage.py makemigrations
	DJANGO_SETTINGS_MODULE=data.settings.local python manage.py migrate

clean:
	docker-compose down

kill:
	docker-compose down --rmi all --remove-orphans

start:
	DJANGO_SETTINGS_MODULE=data.settings.local python manage.py runserver

test:
	@echo "STARTING TEST SUITE\n"
	@echo "UNIT TESTS\n"
	DJANGO_SETTINGS_MODULE=data.settings.test python manage.py test app212

psql:
	docker exec -it $(shell docker-compose ps -q db) psql -Upostgres app212
