#!/usr/bin/env bash
docker ps -a -f status=exited
docker system prune -f
docker rmi postgresql-database
docker build -t postgresql-database:10.0 .

#docker run --detach --name postgresql-database \
#    -p 5432:5432 \
#    postgresql-database:10.0