#!/usr/bin/env bash
docker ps -a -f status=exited
docker system prune -f
docker rmi api-gateway
docker build -t api-gateway:v1 .
#docker run --detach --name api-gateway \
#    -p 8080:8080 \
#    api-gateway:v1


