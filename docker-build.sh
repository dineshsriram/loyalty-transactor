#!/bin/bash

docker build -t dinesh/web -f Dockerfile .
docker build -t dinesh/psql -f old-docker .
