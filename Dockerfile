FROM postgres:latest

ENV POSTGRES_USER 	dinesh
ENV POSTGRES_PASSWORD 	secret
ENV POSTGRES_DB 	loyaltydb

ADD db/loyaltydb.sql	/docker-entrypoint-initdb.d/



