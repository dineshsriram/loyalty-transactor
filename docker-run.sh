#!/bin/sh

docker run -d --name psql -p 0.0.0.0:5432:5432 -t dinesh/psql 
