build:
	docker build -t publications

run:
	docker run -d -p 5000:5000 --name publications publications:latest

stop:
	docker stop publications