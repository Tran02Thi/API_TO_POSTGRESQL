up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

restart:
	make down && make up

run:
	python driver.py --term food --location 'United States' --price 1
	python driver.py --term food --location 'United States' --price 2
	python driver.py --term food --location 'United States' --price 3


