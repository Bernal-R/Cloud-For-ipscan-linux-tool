#!/usr/bin/env bash
docker ps -a -f status=exited
docker system prune -f
docker rmi html
docker build -t html:v1 .
#docker run --detach --name html \
#    -p 8081:8081 \
#    html:v1