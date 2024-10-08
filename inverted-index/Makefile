COMPOSE_FILE = docker-compose.yaml
SERVICE_NAME = inverted-index

.PHONY: all
all: up

.PHONY: up
up:
	@echo "Starting services with Docker Compose..."
	mkdir -p ./input
	cp -r ../data/input/. ./input/
	docker compose -f $(COMPOSE_FILE) up -d
	rm -rf ./input

.PHONY: down
down:
	@echo "Stopping services with Docker Compose..."
	docker compose -f $(COMPOSE_FILE) down

.PHONY: rebuild
rebuild:
	@echo "Rebuilding and starting services..."
	mkdir -p ./input
	cp -r ../data/input/. ./input/
	docker compose -f $(COMPOSE_FILE) up --build -d
	rm -rf ./input

.PHONY: shell
shell:
	@echo "Opening a shell in the $(SERVICE_NAME) container..."
	docker exec -it $(SERVICE_NAME) bash

.PHONY: logs
logs:
	@echo "Showing logs for $(SERVICE_NAME)..."
	docker logs $(SERVICE_NAME) -f

.PHONY: clean
clean:
	@echo "Cleaning up resources..."
	docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: restart
restart: down up
