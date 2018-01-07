#!/bin/sh

docker network create nwapp
docker run -d --name psql --network nwapp -p 0.0.0.0:5432:5432 -t dinesh/psql
docker run -d --name web --network nwapp -p 0.0.0.0:5000:5000 -t dinesh/web
