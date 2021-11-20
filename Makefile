build:
	docker build -t publications

run:
	docker run -d -p 5000:5000 --name publications publications:latest

stop:
	docker stop publications



postgres

build:
	docker build -t postgres

run:
	docker run --name publications.postgres-13.4-alpine -p 5433:5432 -e POSTGRES_PASSWORD=postgres -d postgres:13.4-alpine