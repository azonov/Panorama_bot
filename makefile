# Переменные
IMAGE_NAME=your-telegram-bot
CONTAINER_NAME=telegram-bot-container
DOCKERFILE=Dockerfile
APP_DIR=.

# Docker команды
build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) $(APP_DIR)

run:
	docker run --env-file .env -d --name $(CONTAINER_NAME) $(IMAGE_NAME) 

stop:
	docker stop $(CONTAINER_NAME)

rm:
	docker rm $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Удаление образа
rmi:
	docker rmi $(IMAGE_NAME)

# Полная очистка (стоп и удаление контейнера, затем удаление образа)
clean: stop rm rmi

.PHONY: build run stop rm logs exec clean
