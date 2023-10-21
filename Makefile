build:
	docker compose up --build

daemon:
	docker compose up --build -d

up:
	docker compose up

down:
	docker compose down -v && docker network prune --force

postgres:
	docker exec -it postgres psql -U postgres

bot:
	docker exec -it bot bash

makemigrations:
	docker exec -it bot alembic revision --autogenerate

migrate:
	docker exec -it bot alembic upgrade head